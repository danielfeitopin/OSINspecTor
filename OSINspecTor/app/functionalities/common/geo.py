from flag import flag
from requests import get

def get_geo(dir: str) -> dict:

    def quitar_nulos(foo):
        return foo if foo is not None else 'Desconocido'

    def bandera(foo):
        return flag(foo) if foo is not None else '😔🤟'

    API = 'http://api.ipstack.com/'
    CONSUMER_KEY = '1238e7183b2c121459bf1c32536954e8'
    
    data = get(f'{API}{dir}?access_key={CONSUMER_KEY}')
    if data.status_code == 200:
        info_json = data.json()
        results = {
            'latitude': quitar_nulos(info_json['latitude']),
            'longitude': quitar_nulos(info_json['longitude']),
            'city': quitar_nulos(info_json['city']),
            'region': quitar_nulos(info_json['region_name']),
            'country': quitar_nulos(info_json['country_name']),
            'flag': bandera(info_json['country_code']),  
        }
        status = 200
    else:
        results = f'Error: {data.status_code} {data.reason}'
        status = data.status_code
    return {'results': results, 'status': status}