from bs4 import BeautifulSoup
import requests

# search = input('enter to search: ').strip().replace(' ', "+")
search = 'dog'

# url = f'https://www.google.com/search?q={search}'

"""
def get_html(url):
    return requests.get(url,headers= data).text


def google_images_url(resp_text):
    soup = BeautifulSoup(resp_text, "html.parser")
    a = soup.find_all(attrs = {'id':"top_nav"})
    print(len(a))
    store = a[0].find_all(attrs= {'class': "hide-focus-ring"})
    for x in store:
        print(x.find('span'))
    print(len(store))
    # print(a)
    

google_images_url(get_html(url)
"""

url = 'https://www.google.com/search?q=dots&tbm=isch&ved=2ahUKEwikxqm3yaXuAhWViksFHZlsANQQ2-cCegQIABAA&oq=dots&gs_lcp=CgNpbWcQAzIHCAAQsQMQQzIFCAAQsQMyBQgAELEDMgIIADIFCAAQsQMyAggAMgUIABCxAzICCAAyAggAMgIIADoECAAQQ1CyoQhY6q8IYNGxCGgCcAB4AIABhwKIAfYEkgEFMC4zLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAMABAQ&sclient=img&ei=LYsFYOT7C5WVrtoPmdmBoA0&bih=971&biw=1680'


data = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"}


response = requests.get(url, headers=data)


soup = BeautifulSoup(response.text, "html.parser")

# ["<div><img></div>","<div><img></div>"]
a = soup.find_all(attrs={"class": "bRMDJf islir", "jsname": "DeysSe"})


# print(len(a))
# img_tags = []
for x in a:
    b = x.findAll('img')
    da = b[0]
    data = da.get('src')
    if data == None:
        data = da.get('data-src')
        if data != None:
            print(data)
        else:
            print('no url found')
    else:
        print(data)
    # break

# for x in a:
#     print()
    # b = soup.find('img')
    # print(b)

# with open('file.html', 'w') as file:
#     for x in a:
#         file.write(x.decode('utf-8'))
