import matplotlib.pyplot as plt
import pandas as pd
from base64 import b64encode
from io import BytesIO
from requests import get

def get_subdomains(domain: str) -> dict:

	def get_types_graph(df: pd.DataFrame):
		types = df['type'].value_counts()
		plt.pie(types, labels=types.index, autopct='%1.1f%%')
		plt.title('Subdomain types')
		plt.axis('equal')

		with BytesIO() as buff:
			plt.savefig(buff, format='png')
			plt.clf()
			buff.seek(0)
			figdata = b64encode(buff.read())
			return figdata.decode('utf-8')

	API = 'https://sonar.omnisint.io/all/'

	data = get(f'{API}{domain}')
	if data.status_code == 200:
		info = data.json()
		if info is not None:
			df = pd.DataFrame(info)
			df.drop(columns=['subdomain', 'domain', 'tld'], inplace=True)
			results = {
				'graph': get_types_graph(df),
				'df_dict': df.to_dict(),
			}
			status = 200
		else:
			results = 'No se encontraron subdominios para este dominio.'
			status = 404
	else:
		results = f'Error: {data.status_code} {data.reason}'
		status = data.status_code
	return {'results': results, 'status': status}