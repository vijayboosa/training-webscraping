# import bs4
# import requests


# base_url = "https://www.jiosaavn.com/"


# def write_html(text: str) -> None:
#     with open('jio.html', 'a') as file:
#         file.write(text)


# resp: requests.Response = requests.get(base_url)
# # with open('jio.html', 'w') as file:
# #     file.write(resp.text)

# soup = bs4.BeautifulSoup(resp.text, 'html.parser')


# top_trending = soup.select_one(
#     '#root > div.home.banner > div.u-4\/5-min-vh > div > main > div:nth-child(3) > section > div > div > div > div.o-layout.u-margin-bottom\@sm')

# botton_trending = soup.select_one(
#     "#root > div.home > div.u-4\/5-min-vh > div > main > div:nth-child(3) > section > div > div > div > div:nth-child(2)")

# song_data = top_trending.find_all(
#     attrs={"class": "o-layout__item u-48@sm u-32@md u-1/7@lg"})
# botton_song_data  = botton_trending.find_all(
#     attrs={"class": "o-layout__item u-48@sm u-32@md u-1/7@lg"})

# for x in song_data:
#     print(x.text)

# print('\n'* 2)
# for x in botton_song_data:
#     print(x.text)

# import requests

# resp = requests.get('https://snoidcdnems08.cdnsrv.jio.com/jiosaavn.cdn.jio.com/923/c2c9c47d8c8a51ce2a61ba7ca79e48ca_160.mp4')
# with open('song.mp4', 'wb') as file:
#     file.write(resp.content)