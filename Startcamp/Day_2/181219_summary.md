# 181219 필기

## 1. morning quiz

### 1) 평균을 구하시오

```python
my_score = [79, 84, 66, 93]
my_average = sum(my_score) / len(my_score)
print(my_average)
# print(type(my_average))
```



### 2) 평균을 구하시오

```python
your_score = {
    '수학' : 87,
    '국어' : 83,
    '영어' : 76,
    '도덕' : 100
}

your_average = sum(your_score.values()) / len(your_score)
print(your_average)
# print(type(your_average))

#.values()는 dict_values, .keys()는 dict_keys 타입

```



### 3) 도시의 평균 온도를 구하시오

```python
cities_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}

# # 3 : 도시별 온도 평균
# # 서울: ?
# # 대전: ?
# # 광주: ?
# # 구미: ?

for city, temp in cities_temp.items():
# .items()는 리스트 형식에 튜플로 빼줌
    #     print(city, "의 최근 3일 간 평균 기온은 ", round(sum(temp) / len(temp), 2, "℃  입니다.")
    temp_average = round(sum(temp) / len(temp), 2
    print(city, "의 최근 3일 간 평균 기온은 ", temp_average, "℃  입니다.")

```

#### 선생님 예시

```python
# for city, temperatures in cities_temp.items():
#     print(city + ": " + (sum(temperatures) / len(temperatures)))

# for city in cities_temp:
#     temperatures = cities_temp[city]
#     avg_temperature = round(sum(temperatures) / len(temperatures), 2)
#     print(city, avg_temperature)
#     print(city + ": " + str(avg_temperature))
#     print("{0}: {1}".format(city, avg_temperature))
```





### 4) 가장 더운 도시, 가장 추운 도시를 구하시오

```python
# 4: 도시 중에 최근 3일 간 가장 추웠던 곳과 가장 더웠던 곳
# Hottest : ?, Coldest : ?

city_list = []
temp_list = []
for city, temp in cities_temp.items():
    city_list.append(city)
    temp_list.append(max(temp))

print("가장 더운 도시는 ", city_list[temp_list.index(max(temp_list))], "이고 ", max(temp_list), "℃  입니다.")

for city, temp in cities_temp.items():
    city_list.append(city)
    temp_list.append(min(temp))

print("가장 추운 도시는 ", city_list[temp_list.index(min(temp_list))], "이고 ", min(temp_list), "℃  입니다.")
```

#### 선생님 예시

```python
# all_temp 에 모든 기온을 모은다
all_temp = []
for key, value in cities_temp.items():
    all_temp += value

# all_temp 에서 highest/lowest 를 찾는다
highest = max(all_temp)
lowest = min(all_temp)
print(highest, lowest)

# cities_temp 에서 highest/lowest 가 속한 도시를 찾는다
hottest = []
coldest = []
for key, value in cities_temp.items():
    if highest in value:
        hottest.append(key)
    if lowest in value:
        coldest.append(key)

print(hottest, coldest)
```



## 2. codecademy

### 1) Cloud9

- C9 ! C9 ! c9.io

### 2) codecademy

- html 보기
