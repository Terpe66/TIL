import os
import csv
import requests
from time import *
from datetime import *

kobis_data = []
key = os.getenv("KOBIS_KEY")
url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&weekGb=0&targetDt="

count = 0
while len(kobis_data) < 10:
    day = str(datetime(2019, 1, 13) - timedelta(count * 7))[:10].replace("-", "")
    kobis_data.append(requests.get(url + day).json()["boxOfficeResult"])
    count += 1
kobis_data = list(reversed(kobis_data))

kobis_list = []
for kobis_d in kobis_data:
    for kobis in kobis_d["weeklyBoxOfficeList"]:
        add = [kobis["movieCd"], kobis["movieNm"], kobis["audiAcc"], kobis_d["showRange"][9:]]
        if kobis_list == []:
            kobis_list.append(add)
        else:
            for idx in range(len(kobis_list)):
                if add[0] in kobis_list[idx]:
                    kobis_list[idx] = add
                    break
            else:
                kobis_list.append(add)

csvwrite = open("boxoffice.csv", "a+", encoding="utf-8", newline="")
csvwriter = csv.writer(csvwrite)
csvwriter.writerow(["영화 대표코드", "영화명", "누적 관객수", "해당일"])

for i in kobis_list:
    csvwriter.writerow(i)

csvwrite.close()


csvread = open("boxoffice.csv", "r", encoding="utf-8", newline="")
csvreader = csv.reader(csvread)

movie_info = []
for l in csvreader:
    if "영화 대표코드" not in l:
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={l[0]}"
        movie_info.append(requests.get(url).json())

csvread.close()

Movie_info = []
for movie in movie_info:
    Movie_info.append(movie["movieInfoResult"]["movieInfo"])

info_list = []
for info in Movie_info:
    if len(info["actors"]) >= 3:
        info_list.append([
            info["movieCd"], info["movieNm"], info["movieNmEn"], info["movieNmOg"], 
            info["openDt"], info["showTm"], info["genres"][0]["genreNm"], 
            info["directors"][0]["peopleNm"], info["audits"][0]["watchGradeNm"],
            info["actors"][0]["peopleNm"], info["actors"][1]["peopleNm"], info["actors"][2]["peopleNm"]])
    elif len(info["actors"]) == 2:
        info_list.append([
            info["movieCd"], info["movieNm"], info["movieNmEn"], info["movieNmOg"], 
            info["openDt"], info["showTm"], info["genres"][0]["genreNm"], 
            info["directors"][0]["peopleNm"], info["audits"][0]["watchGradeNm"],
            info["actors"][0]["peopleNm"], info["actors"][1]["peopleNm"], ""])
    elif len(info["actors"]) == 1:
        info_list.append([
            info["movieCd"], info["movieNm"], info["movieNmEn"], info["movieNmOg"], 
            info["openDt"], info["showTm"], info["genres"][0]["genreNm"], 
            info["directors"][0]["peopleNm"], info["audits"][0]["watchGradeNm"],
            info["actors"][0]["peopleNm"], "", ""])    
    elif len(info["actors"]) == 0:
        info_list.append([
            info["movieCd"], info["movieNm"], info["movieNmEn"], info["movieNmOg"], 
            info["openDt"], info["showTm"], info["genres"][0]["genreNm"], 
            info["directors"][0]["peopleNm"], info["audits"][0]["watchGradeNm"],
            "", "", ""])
    

csvwrite = open("movie.csv", "a+", encoding="utf-8", newline="")
csvwriter = csv.writer(csvwrite)
csvwriter.writerow(["영화 대표코드", "영화명(국문)", "영화명(영문)", "영화명(원문)", 
                 "개봉연도", "상영시간", "장르",
                 "감독명", "관람등급", 
                 "배우1", "배우2", "배우3"])

for i in info_list:
    csvwriter.writerow(i)

csvwrite.close()


csvread = open("movie.csv", "r", encoding="utf-8", newline="")
csvreader = csv.reader(csvread)

movie_info = []
for l in csvreader:
    if "영화 대표코드" not in l:
        movie_info.append([l[0], l[1]])

csvread.close()


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
    Movie_info["userRating"] = naver_data["items"][0]["userRating"]
    naver_info.append(Movie_info)
    sleep(0.05)

csvwrite = open("movie_naver.csv", "a+", encoding="utf-8", newline="")
csvwriter = csv.writer(csvwrite)
csvwriter.writerow(["영화명(국문)", "영화 대표코드", "영화 썸네일 이미지 URL", "영화 하이퍼링크", "유저 평점"])

for i in range(len(naver_info)):
    csvwriter.writerow([naver_info[i]["title"], movie_info[i][0], naver_info[i]["image"], naver_info[i]["link"], naver_info[i]["userRating"]])

csvwrite.close()


os.mkdir("./images/")
csvread = open("movie_naver.csv", "r", encoding="utf-8", newline="")
csvreader = csv.reader(csvread) 

for l in csvreader:
    if "영화명(국문)" not in l:
        with open(f"./images/{l[1]}.jpg", "wb") as file:
            img_res = requests.get(l[2])
            file.write(img_res.content)

csvread.close()

