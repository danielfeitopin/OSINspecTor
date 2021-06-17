import googlesearch
import re
import requests
from bs4 import BeautifulSoup
from pandas import Series

def get_emails(domain: str) -> dict:

    def email_on_url(page, domain):
        soup = BeautifulSoup(page.text, 'html.parser')
        return re.findall(f"[A-Za-z0-9.]+@{domain}", soup.get_text())

    def search_in_google(query: str):
        return googlesearch.search(query, tld="com", num=20, stop=20, pause=2)

    sercode=True
    try:    
        lista = []
        for j in search_in_google(f'intext:"@{domain}"'):
            if re.search("\.pdf$", j) is None:
                try:
                    page = requests.get(j)
                    lista+=email_on_url(page, domain)
                except:
                    pass
        if lista == []:
            sercode=False
            raise Exception("No se encontraron resultados para ese dominio.")
        series = Series(lista).sort_values().drop_duplicates()
        series = series.reset_index(drop=True).to_dict()
        results = series
        status = 200

    except Exception as e:
        if sercode:
            results = 'Este servicio no está disponible en este momento:'
            status = 429
        else:
            results = f'{e}'
            status = 404
    finally:
        return {'results': results, 'status': status}