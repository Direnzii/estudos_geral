from os import getenv
from shodan import Shodan
import requests
from scrapy.selector import Selector

my_key_shodan = getenv(key='CHAVE_SHODAN')
api = Shodan(my_key_shodan)

host_common = 'www.facebook.com'
api_whois = f'https://rst.im/dig/{host_common}/default/noshort/notrace/?type='

url_whois = 'https://who.is/whois/'
ip = ''
buscar = 'www.uol.com'

try:
    host = api.host(ip)
    teste = api.exploits
    # Print general info

    print(teste)
    print('host:', host['ip_str'],
          host['org'], host['city'],
          host['region_code'],
          host['isp'],
          host['latitude'],
          host['longitude'],
          host['ports'],
          host['country_name'],
          host['country_code'],
          '\n')

    for item in host['data']:
        print(item['port'], item['data'])
except:
    print('IP não localizado ou não é válido')

status_code_whois = requests.get(url_whois + buscar).status_code

a = requests.get(api_whois).text
selector_txt = Selector(text=a)
print(selector_txt.css('.col-lg-8 > pre:nth-child(1) > code:nth-child(1)').extract()[0])


if status_code_whois == 200:
    print(url_whois + buscar)