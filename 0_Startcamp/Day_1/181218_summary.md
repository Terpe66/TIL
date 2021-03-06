# 181218 수업정리

## 1. 개발환경설정

+ choholatey
  + 윈도우 패키지 매니저
+ python -V 3.6.7
+ git
  + Version Consol System
+ vscode
  + Code Editior
+ Chrome
  + Browser



## 2. list

### list 만들기

```python
MCU = [
    ["Ironman", "Captain America", "Thor", "Hulk", "Dr.Strange"],
    ["Xmen", "Deadpool"],
    ["Spiderman"]
    ]
disney = MCU[0]
#disney[1] = Captain America
#MCU[0][1] = Captain America
```



### list 추출하기

1. `[0]`처럼 인덱스 접근하기
2. `[1:10]`처럼 잘라내기
3. 2의 경우, 슬라이싱은 1개든 여러 개든 리스트로 추출



### list 더하기

1. 리스트끼리 +연산을 하면 리스트가 리스트의 안으로 가는 게 아니라 리스트 안에 값으로 들어감
2. 리스트 안에 리스트를 추가하려면 .append() 쓰거나 [[]] 방식으로 입력



## 3. dict

### 리스트 안의 딕셔너리 안의 정보 추출하기

```python
info = {
    'name' : 'ryan', 
    'job':'character',
    'mobile' : '12345678',
    'email' : 'ryan@kakao.kr'
}

info = [
    {'name' : 'Lee', 
    'email' : 'Lee@naver.com'}, 
    {'name' : 'Park', 
    'email' : 'Park@naver.com'}, 
    {'name' : 'Kim', 
    'email' : 'Kim@naver.com'}
]

print(info[2]['name'])
```



1. 가장 현실의 정보를 담기 좋은 게 딕셔너리
2. key는 대부분 str, value는 다양



## 4. Function

### 정렬

1. sorted() 사용
2. .sort() 사용
3. 역정렬시엔 sorted(값, reverse=True) 사용, 기본은 reverse=False, 혹은 .sort() 후 .reverse()



```python
print("Cap")
len("Cap")
# 3 추출
len(["C", "a", "p", "t", "a", "i", "n"])
# 7 추출
del()
type("Captain")

scores = [45, 60, 78, 98, 88]
high_score = max(scores)
lowest_score = min(scores)
print(lowest_score)
#print(high_score)
#print(sorted(scores)[-1])

#round(1.28569, 2)
# 2번째 자리까지 반올림
#ceil / floor 올림 버림

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# full 에 first 와 second 를 합쳐서 저장
full = first + second
print(full)

# full_sorted 에 full 을 정렬해서 저장
full_sorted = sorted(full)
print(full_sorted)

# *reverse_sorted 에 full 을 내림차순으로 정렬해서 저장
reverse_sorted = sorted(full, reverse=True)
print(reverse_sorted)
```



## 5. method

```python
my_list = [4, 7, 9, 1, 3, 6]

# 최대/최소
max(my_list)
min(my_list)

# 특정 요소의 인덱스, my_list 안의 3이 몇 번째에 있는지
my_list.index(3)

# 리스트를 뒤집으려면?
my_list.reverse()

dust = 100
# class : int, 위의 100은 int object라고 부름
lang = 'python'
# class : str, 위의 'python'은 str object라고 부름
samsung = ['elec', 'sds', 's1']
# class : list

samsung.index('sds')
samsung.count('sds')

lang.capitalize()
# 첫 글자를 대문자로 바꾸는데 저장은 아님

lang.replace('on', 'off')
# 문자열 바꾸기, 저장 안 됨

```



1. method가 바꾸고 저장하는 경우와 저장 안 하고 뱉어내기만 하는 경우가 있음
2. .append()는 원본이 변경된다
3. [주어].동사()의 형식으로 이루어지며, [주어] 자리에 오는 object들이 할 수 있는 행동(함수)들이다



| str        | int  | list                   | bool   | Class      |
| ---------- | ---- | ---------------------- | ------ | ---------- |
| `'python'` | `23` | `[Samsung, LG, Apple]` | `True` | **Object** |



## 6. 크롤링

### 로또 번호 조회, 랜덤 생성한 숫자와 비교하기

```python
import requests

url = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"

response = requests.get(url, verify = False)
print(response.text)
```



1. pip install requests 설치 후 import
2. requests.get(주소)
3. print(requests.get(주소, verify = False)), verify = False는 안전검사 패스



### for in / if

```python
import requests

url = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"

response = requests.get(url, verify = False)
#print(response.text)

data = response.json()

real_numbers = []
# for key in data:
#     if 'drwtNo' in key:
#         real_numbers.append(data[key])

for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)
# .items() 는 key와 value를 튜플()로 묶은 값을 dict_items 객체로 반환한다.

real_numbers.sort()
print(real_numbers)
```

1. for in / if, list일 땐 요소, dict일 땐 키



## git 관리

```
student@M70313 MINGW64 ~/TIL
$ ls
Startcamp

student@M70313 MINGW64 ~/TIL
$ pwd
/c/Users/student/TIL

student@M70313 MINGW64 ~/TIL
$ git init
Initialized empty Git repository in C:/Users/student/TIL/.git/

student@M70313 MINGW64 ~/TIL (master)
$ ls -a
.  ..  .git  Startcamp

student@M70313 MINGW64 ~/TIL (master)
$ rm -rf .git/

student@M70313 MINGW64 ~/TIL
$ ls -a
.  ..  Startcamp

student@M70313 MINGW64 ~/TIL
$ git init
Initialized empty Git repository in C:/Users/student/TIL/.git/

student@M70313 MINGW64 ~/TIL (master)
$ git config --global user.name 'Wonjin'

student@M70313 MINGW64 ~/TIL (master)
$ git config --global user.email 'terpe66@gmail.com'

student@M70313 MINGW64 ~/TIL (master)
$ git add .

student@M70313 MINGW64 ~/TIL (master)
$ git commit -m '~181218'
[master (root-commit) d6a7579] ~181218
 15 files changed, 499 insertions(+)
 create mode 100644 Startcamp/Day_1/.vscode/settings.json
 create mode 100644 "Startcamp/Day_1/181218 \354\210\230\354\227\205\354\240\225\353\246\254.md"
 create mode 100644 Startcamp/Day_1/am_i_lucky.py
 create mode 100644 Startcamp/Day_1/dict.py
 create mode 100644 Startcamp/Day_1/first_python.py
 create mode 100644 Startcamp/Day_1/function.py
 create mode 100644 Startcamp/Day_1/get_lotto.py
 create mode 100644 Startcamp/Day_1/list1.py
 create mode 100644 Startcamp/Day_1/list2.py
 create mode 100644 Startcamp/Day_1/method.py
 create mode 100644 Startcamp/Day_1/pick_lotto.py
 create mode 100644 Startcamp/Day_1/test_lotto.py
 create mode 100644 Startcamp/Day_1/weather.py
 create mode 100644 Startcamp/Day_1/web_browser.py
 create mode 100644 Startcamp/__pycache__/webbrowser.cpython-36.pyc

student@M70313 MINGW64 ~/TIL (master)
$ git log
commit d6a75795e4bf4444d1baa77c28e12125388dbffe (HEAD -> master)
Author: Wonjin <terpe66@gmail.com>
Date:   Tue Dec 18 17:45:17 2018 +0900

    ~181218

student@M70313 MINGW64 ~/TIL (master)
$ git remote add origin https://github.com/Terpe66/TIL.git

student@M70313 MINGW64 ~/TIL (master)
$ git push -u origin master
Enumerating objects: 21, done.
Counting objects: 100% (21/21), done.
Delta compression using up to 12 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (21/21), 6.01 KiB | 2.00 MiB/s, done.
Total 21 (delta 0), reused 0 (delta 0)
To https://github.com/Terpe66/TIL.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

```

