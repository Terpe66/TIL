import os
import requests
import urllib.request
import csv
import time


f_r = open("movie.csv", "r", encoding="utf-8", newline="")
reader = csv.reader(f_r)

movie_info = []
for line in reader:
    if "영화 대표코드" not in line:
        movie_info.append([line[0], line[1]])
    
f_r.close()

print(movie_info)
print(len(movie_info))

url = "https://openapi.naver.com/v1/search/movie.json?query="

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")

headers = {
    "X-Naver-Client-Id": client_id,
    "X-naver-Client-Secret": client_secret
}

naver_info = []
for movie in movie_info:
    naver_data = requests.get(url + movie[1], headers=headers).json()
    Movie_info = {}
    Movie_info["title"] = naver_data["items"][0]["title"].lstrip("<b>").rstrip("</b>")
    Movie_info["link"] = naver_data["items"][0]["link"]
    Movie_info["image"] = naver_data["items"][0]["image"]
    naver_info.append(Movie_info)
    time.sleep(0.05)



f_w = open("movie_naver.csv", "a+", encoding="utf-8", newline="")
writer = csv.writer(f_w)
writer.writerow(["영화명(국문)", "영화 대표코드", "영화 썸네일 이미지 URL", "영화 하이퍼링크", "유저 평점"])

for i in range(len(naver_info)):
    writer.writerow([naver_info[i]["title"], movie_info[i][0], naver_info[i]["image"], naver_info[i]["link"], naver_info[i]["userRating"]])

f_w.close()

f_r = open("movie_naver.csv", "r", encoding="utf-8", newline="")
reader = csv.reader(f_r)

for l in reader:
    if "영화명(국문)" not in l:
        with open(f"./images/{l[1]}.jpg", "wb") as file:
            img_res = requests.get(l[2])
            file.write(img_res.content)

f_r.close()