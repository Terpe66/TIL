# import requests
# #requests 모듈 부르기
# from bs4 import BeautifulSoup
# #bs4 모듈에서 BeautifulSoup만 부르기

# response = requests.get("https://finance.naver.com/sise/")
# #requests 함수에 도메인 입력해서 부르기
# doc = response.text
# #부른 도메인을 텍스트화해서 doc에 입력

# soup = BeautifulSoup(doc, "html.parser")
# #BeautifulSoup을 이용해서 soup에 입력
# kospi = soup.select_one("#KOSPI_now")
# #select_one 함수에 코스피지수 id를 입력해서 부르기, #은 아이디의 의미

# print(kospi.text)
# #코스피지수 부르기

# kospi = soup.select_one("#KOSPI_now").text
# print(kospi)

# url = "https://finance.naver.com/marketindex/"

# response = requests.get(url).text
# soup = BeautifulSoup(response, "html.parser")

# data_set = soup.select(".value")
# #select 함수로 value 클래스 전체를 부르기, .은 class의 의미
# data = data_set[1].text
# print(data_set)
# # print("JPY")
# # print(data)


import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.laliga.es/laliga-santander")
url_doc = response.text

parser_doc = BeautifulSoup(url_doc, "html.parser")
rank_data = parser_doc.select(".nombre-equipo-clasificacion")

# print(rank_data[19].text)
A = list(range(0, 20))



print(point)

# for a in A:
#     print(point_data[a].text)

