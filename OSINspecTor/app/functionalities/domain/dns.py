import pandas as pd
from json import loads
from requests import get

def get_dns(domain: str) -> dict:

    API = 'https://freeapi.robtex.com/pdns/forward/'

    data = get(f'{API}{domain}')
    if data.status_code == 200:
        if data.text != '':
            info = [loads(entry)
                for entry in data.text.split("\r\n")
                if entry != '']
            df = pd.DataFrame(info)[['rrname', 'rrdata', 'rrtype']]
            df = df[df['rrtype']=='NS']
            results = list(df['rrdata'].values)
            status = 200
        else:
            results = "No se encontraron resultados para este dominio."
            status = 404
    else:
        results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    return {'results': results, 'status': status}