import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.premierleague.com/")
url_doc = response.text

parser_doc = BeautifulSoup(url_doc, "html.parser")
rank_data = parser_doc.select(".team")

print(rank_data[1].text)


# url = "https://finance.naver.com/marketindex/"

# response = requests.get(url).text
# soup = BeautifulSoup(response, "html.parser")

# data_set = soup.select(".value")
# #select 함수로 value 클래스 전체를 부르기, .은 class의 의미
# data = data_set[1].text
# print("JPY")
# print(data)
