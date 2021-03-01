import requests
from bs4 import BeautifulSoup

# url of job website
url = 'https://www.freejobalert.com/'


response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')

# print(dir(soup))
a = soup.find('table', {'class': 'listcontentj'})
# print(a.prettify())
tr = a.find_all('tr')[0]
td = a.find('td')
a_tag = td.find_all('a')
for x in a_tag:

    text = x.text.lower()
    link = x.get('href')
    if ('indian' in text) or ('army' in text) or ('air force' in text) or ('airforce' in text):
        print(text)
        print(link)
