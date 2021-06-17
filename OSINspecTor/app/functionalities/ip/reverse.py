from requests import get

def get_reverse(ip: str) -> dict:

    REVURL = 'https://sonar.omnisint.io/reverse/'

    data = get(f'{REVURL}{ip}')
    if data.status_code == 200:
        info = data.json()
        if info is None:
            results = 'Esta IP no tiene un nombre de dominio asociado.'
            status = 404
        elif len(info) != 1:
            results = 'Esta IP no tiene un único nombre de dominio.'
            status = 404
        else:
            results = info
            status = 200
    else:
        results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    return {'results': results, 'status': status}