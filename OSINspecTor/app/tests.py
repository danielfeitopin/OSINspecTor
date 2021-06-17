from django.http import response
from django.test import TestCase
from app.functionalities.common import geo
from app.functionalities.common import vuln
from app.functionalities.domain import dns
from app.functionalities.ip import reverse
from app.functionalities.domain import mx
from app.functionalities.domain import range
from app.functionalities.domain import subdomains
from app.functionalities.domain import emails
# Create your tests here.
#vistas

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
    def test_domain_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/dominio/')
        self.assertEqual(response.status_code, 200)
    def test_IP_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/ip/')
        self.assertEqual(response.status_code, 200)
    def test_no_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/efwf')
        self.assertEqual(response.status_code, 404)

#funciones
class GeoDomainTestCase(TestCase):
    def test_dom_geo(self):
        info = geo.get_geo("udc.es")
        self.assertEqual(str(info), "{'results': {'latitude': 43.37126159667969, 'longitude': -8.389616012573242, 'city': 'A Coruña', 'region': 'Galicia', 'country': 'Spain', 'flag': '🇪🇸'}, 'status': 200}")
    def test_ip_geo(self):
        info = geo.get_geo("193.144.53.84")
        self.assertEqual(str(info), "{'results': {'latitude': 43.371490478515625, 'longitude': -8.395970344543457, 'city': 'A Coruña', 'region': 'Galicia', 'country': 'Spain', 'flag': '🇪🇸'}, 'status': 200}")

class  VulDomainTestCase(TestCase):
    def test_dom_vuln(self):
        info = vuln.get_vulns("udc.es")
        self.assertEqual(str(info), "{'results': {'ports': [80, 443], 'vulns': None}, 'status': 200}")
    def test_ip_vuln(self):
        info = vuln.get_vulns("193.144.53.84")
        self.assertEqual(str(info), "{'results': {'ports': [80, 443], 'vulns': None}, 'status': 200}")

class DnsDomainCase(TestCase):
    def test_dns(self):
        info = dns.get_dns("udc.es")
        if info["status"] == 200:
                self.assertEquals(str(info),"{'results': ['ineco.nic.es', 'nso.nic.es', 'chico.rediris.es', 'sun.rediris.es', 'zape.udc.es', 'zipi.udc.es'], 'status': 200}")
        else:
            if info["status"] == 429:
                self.assertEquals(str(info), "{'results': 'Error: 429 Too Many Requests', 'status': 429}")
            else:
                self.assertEqual(info["status"], 404)
        

class RevIPCaseNoDomain(TestCase):
    def test_rev(self):
        info = reverse.get_reverse("8.8.8.8")
        self.assertEqual(str(info), "{'results': 'Esta IP no tiene un nombre de dominio asociado.', 'status': 404}")
    def test_rev(self):
        info = reverse.get_reverse("74.125.206.138")
        self.assertEqual(str(info), "{'results': ['wk-in-f138.1e100.net'], 'status': 200}")

class MxDomainCase(TestCase):
    def test_mx(self):
        info = mx.get_mx("udc.es")
        if info["status"] == 200:
            self.assertEquals(str(info),"{'results': ['mail.rediris.es', 'mx.udc.es', 'mx2.udc.es', 'udc-es.mail.protection.outlook.com'], 'status': 200}")
        else: 
            if info["status"] == 429:
                self.assertEquals(str(info), "{'results': 'Error: 429 Too Many Requests', 'status': 429}")
            else:
                self.assertEqual(info["status"], 404)

class RangeDomainCase(TestCase):
    def test_range(self):
        info = range.get_range("udc.es")
        self.assertEqual(str(info),"{'results': '193.144.48.0 - 193.144.63.255', 'status': 200}")

class EmailsDomainCase(TestCase):
    def test_email(self):
        info = emails.get_emails("udc.es")
        if info["status"] == 200:
            self.assertEqual(info["status"],200)
        else:
            if info["status"] == 429:
                self.assertEqual(str(info),"{'results': 'Este servicio no está disponible en este momento:', 'status': 429}")
            else:
                self.assertEqual(info["status"], 404)

        
class SubDomainCase(TestCase):
    def test_subdomains(self):
        info = subdomains.get_subdomains("udc.es")
        if info["status"] == 200:
            self.assertEqual(info["status"], 200)
        else:
            self.assertEqual(info["status"], 404)