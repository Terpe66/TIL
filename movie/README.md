# Movie Info Crawling

## KOBIS

### 1. 영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터)

1) kobis의 api를 활용해 2018년 11월 11일부터 10주차인 2019년 1월 13일까지의 영화 정보를 크롤링, 링크의 default 값은 주말(금토일)만 반영되어 `&weekGb=0`을 추가

2) 주간 박스오피스의 json 정보를 크롤링 한 뒤 뒤 영화 대표코드("movieCd"), 영화명("movieNm"), 해당일 누적 관객수("audiAcc"), 해당일("showRange")을 `list`에 추가

3) 누적 관객수 최신화를 위해 대표코드가 같으면 그 index에 최신 정보를 덮어씀

4) boxoffice.csv에 저장

### boxoffice.csv

1) 영화 대표코드, 영화명, 누적 관객수, 해당일 순으로 정렬

   ```
20177538,완벽한 타인,5270621,20181216
20185485,보헤미안 랩소디,9785643,20190113
20170513,동네사람들,445625,20181118
	...
	...
20176251,내안의 그놈,765383,20190113
20183915,극장판 공룡메카드: 타이니소어의 섬,289873,20190113
20184574,그린 북,99569,20190113
   ```

2) 10주차 100개의 영화 중 중복된 영화를 제외한 43개 영화가 저장됨



### 2. 영화진흥위원회 오픈 API(영화 상세정보)

1) boxoffice.csv의 내용(영화 대표코드)을 상세정보 url에 활용해서 43개 영화의 상세정보를 크롤링

2) 배우가 3명 이상인 경우, 2명인 경우, 1명인 경우, 0명인 경우로 나누어 movie.csv에 저장

### movie.csv

1) 영화 대표코드, 영화명(국문), 영화명(영문), 영화명(원문), 개봉연도, 상영시간, 장르, 감독명, 관람등급, 배우1, 배우2, 배우3 순으로 정렬

```
20177538,완벽한 타인,Intimate Strangers,,20181031,115,드라마,이재규,15세이상관람가,유해진,조진웅,이서진
20185485,보헤미안 랩소디,Bohemian Rhapsody,,20181031,134,드라마,브라이언 싱어,12세이상관람가,레미 맬렉,조셉 마젤로,마이크 마이어스
20170513,동네사람들,,,20181107,99,액션,임진순,15세이상관람가,마동석,김새론,이상엽
	...
	...
20176251,내안의 그놈,Inside me,,20190109,122,판타지,강효진,15세이상관람가,박성웅,진영,라미란
20183915,극장판 공룡메카드: 타이니소어의 섬,,,20190110,70,애니메이션,최신규,전체관람가,,,
20184574,그린 북,Green Book,,20190109,130,드라마,피터 패럴리,12세이상관람가,비고 모텐슨,마허샬라 알리,
```

2) 비어있는 항목은 ""으로 처리되어 있어서 배우 정보가 없는 영화도 배우 항목을 ""처리



## Naver
### 3. 네이버 영화 검색 API

1) movie.csv의 영화명(국문)을 네이버 API에 활용해서 영화의 썸네일 이미지 URL, 하이퍼링크, 유저 평점을 크롤링

2) 영진위 영화 대표코드, 영화 썸네일 이미지 URL, 하이퍼링크, 유저 평점 순으로 movie_naver.csv에 저장

### movie_naver.csv

1) 영화 대표코드, 썸네일 이미지 URL, 하이퍼링크, 유저 평점만 텍스트로 있으면 어떤 영화의 정보인지 알 수 없기 때문에 가장 앞에 영화명(국문) 추가

```
완벽한 타인,20177538,https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167638_P71_133542.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=167638,8.66
보헤미안 랩소디,20185485,https://ssl.pstatic.net/imgmovie/mdi/mit110/1564/156464_P49_182103.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=156464,9.47
동네사람들,20170513,https://ssl.pstatic.net/imgmovie/mdi/mit110/1666/166610_P58_154049.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=166610,5.52
	...
	...
내안의 그놈,20176251,https://ssl.pstatic.net/imgmovie/mdi/mit110/1641/164172_P26_152224.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=164172,8.76
극장판 공룡메카드: 타이니소어의 섬,20183915,https://ssl.pstatic.net/imgmovie/mdi/mit110/1803/180372_P16_101254.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=180372,9.19
그린 북,20184574,https://ssl.pstatic.net/imgmovie/mdi/mit110/1715/171539_P26_135622.jpg,https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539,9.66
```



### 4. 영화 포스터 이미지 저장

1) movie_naver.csv의 영화 썸네일 이미지 URL을 활용해 각 영화의 썸네일 이미지를 크롤링

2) images 폴더 안에 영화 대표코드.jpg로 저장

```python
f_r = open("movie_naver.csv", "r", encoding="utf-8", newline="")
reader = csv.reader(f_r)

for l in reader:
    if "영화명(국문)" not in l:
        with open(f"./images/{l[1]}.jpg", "wb") as file:
            img_res = requests.get(l[2])
            file.write(img_res.content)

f_r.close()
```

