from random import randrange
from requests import get
from socket import gethostbyname

def get_vulns(dir: str)  -> dict:

    def get_results(info_json: dict, key: str):
        if key in info_json:
            param = info_json[key]
            param.sort()
        else:
            param = None
        return param

    API = 'https://api.shodan.io/shodan/host/'  
    CONSUMER_KEYS = [
        'FrrnWjvV9B3u0Ioi2VjEdIcOgqa9PLDM',
        '0SyRpxwejxcTAyUWhQ7v7BLAla9y12XD',
        '74CkfufwScfxmaAY7MUmAftDE9lX5TGE',
        '2iIkq0lA64RipatiHx9YtNxieBpjRqor',
        'RGA9cuLe2xkxBjmregqGrlDM0valZBuY',
        'ZDZZNY7abyomOHsz9d3jCsfT3HXB5Htu',
    ]
    try:
        dir= gethostbyname(dir)
    except:
        dir = 'invalidquery'

    key = CONSUMER_KEYS[randrange(len(CONSUMER_KEYS))]
    data = get(f'{API}{dir}?key={key}')
    if data.status_code == 200:
        results = {
            'ports': get_results(data.json(), 'ports'),
            'vulns': get_results(data.json(), 'vulns')
        }
        status = 200
        if results['ports'] is None and results['vulns'] is None:
            results = "No se encontraron resultados."
            status = 404
    elif data.status_code == 404:
        results =  'No se encontraron puertos abiertos ni vulnerabilidades.'
        status = 404
    else:
        results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    return {'results': results, 'status': status}
