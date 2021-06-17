from requests import get
from socket import gethostbyname

def get_range(domain: str) -> dict:

    API = 'https://rest.db.ripe.net/search.json?query-string='
    FLAGS = '&type-filter=inetnum&flags=no-referenced&flags=no-irt&source=RIPE'

    try:
        param = gethostbyname(domain)
    except:
        param = 'invalidquery'

    data = get(f'{API}{param}{FLAGS}')
    if data.status_code == 200:
        info = data.json()
        info = info['objects']['object'][0]
        info = info['primary-key']['attribute'][0]
        info = info['value']
        results = info
        status = 200
    elif data.status_code == 404:
        results =  'No se encontro el rango de IPs asociado a este dominio.'
        status = 404
    else:
        results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    return {'results': results, 'status': status}