import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from collections import defaultdict
import time

start_time = time.time()
master_dict = []
dd = defaultdict(list)
def getInfo(x):
    url = (f'{x}')
    d = {}
    headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
               'referer' : 'https://cdn.kyruus.com/pmc-customer-static-assets/sclhealth/header-footer-style/2.2/header-footer-style.css'}
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('h2',{'id':'provider-name'})
    street = soup.find_all('span', {'itemprop':'streetAddress'})
    specialty = soup.find('span', {'itemprop':'medicalSpecialty'})
    city = soup.find_all('span', {'itemprop':'addressLocality'})
    s_zip = soup.find_all('span', {'itemprop':'postalCode'})
    state = soup.find_all('span', {'itemprop':'addressRegion'})
    link =  soup.find('div',{'id':'about-panel-external_links'})
    c = re.search('href=(\S*)',str(link))
    #print(c[0])
    if c is None:
        website = 'None'
    else:
        website = c[0]
    remove = ['href=','>','Visit','SCL', '"']
    for char in remove:
        website = website.replace(char,'')
    total_locations = soup.find_all('h2', {'class':'fw-6 fs-s location-title'})
    if len(total_locations) > 0: #Can be made more effcient by adding else statement
        di = {}
        for r in range(len(total_locations)):
            di[r] = {}
            di[r] = {'Name':f'{name.text}',
                     'Group':f'{total_locations[r].text}',
                     'Specialty':f'{specialty.text}',
                     'Street':f'{street[r].text}',
                     'City':f'{city[r].text}',
                     'Zip':f'{s_zip[r].text}',
                     'State':f'{state[r].text}',
                     'Website':f'{website}'}
            for k,v in di[r].items():
                dd[k].append(v)
    return dd
 
url = 'https://doctors.sclhealth.org/search?sort=networks%2Crelevance%2Cavailability_density_best'
headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
           'referer' : 'https://cdn.kyruus.com/pmc-customer-static-assets/sclhealth/header-footer-style/2.2/header-footer-style.css'}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('h2', {'class':'css-1yi8h8m-ProviderName e16v8r6n5'})
base = 'https://doctors.sclhealth.org'
for po in links:
    match = re.findall('href=(\S*)',str(po))
    cl_match = match[0].replace('"', '')
    new_link = base + cl_match
    #print(new_link)
    getInfo(new_link)
print(pd.DataFrame(dd))
print('--- %s seconds ---' % (time.time() - start_time))