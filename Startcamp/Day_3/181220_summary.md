# 181220 수업정리

## 1. HTML

- <h?> tag는 뼈대, 각 tag의 의미를 보자
- Introduction, CSS 보기



## 2. 로또

### 1) 선생님 답안

```python
# 선생님 답안
count = 0
for my_number in my_numbers:
    for real_number in real_numbers:
        if my_number == real_number:
            count += 1

print(count)

#set를 사용해서도 할 수 있음
```



### 2) function으로 만들기(pick_lotto(), get_lotto())

```python
import requests
import random

def pick_lotto():
    # numbers = random.sample(range(1, 46))
    numbers = random.sample(range(1, 46), 6)
# range는 정수 리스트로 뽑음, 위는 list(range(1, 46))으로 안 써도 됨
    return numbers
# sotred()는 반환을 하고, .sort()는 반환하지 않음

my_numbers = pick_lotto()
print(my_numbers)


def get_lotto():
    url = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"
    response = requests.get(url, verify = False)
    lotto_data = response.json()
    
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    
    numbers.sort()
    bonus_number = lotto_data['bnusNo']
    final_dict = {"numbers" : numbers, "bonus" : bonus_number}

    return final_dict

real_numbers = get_lotto()
print(real_numbers)

```

### 3) 통합해서 만들기(am_i_lucky(draw_no)

```python
def am_i_lucky(draw_no):
	my_numbers = random.sample(range(1, 46), 6)
	if type(draw_no) == int:
		url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(draw_no)
		response = requests.get(url)
		lotto_data = response.json()
		numbers = []
		for key, value in lotto_data.items():
			if 'drwtNo' in key:
				numbers.append(value)
		bonus_number = lotto_data['bnusNo']
		real_numbers = {"numbers" : numbers, "bonus" : bonus_number}
	else:
		print("숫자를 입력해주세요.")
	count = 0
	for lucky_number in my_numbers:
		if lucky_number in real_numbers["numbers"]:
			count += 1
	if count == 6:
		print("1등")
	elif count == 5 and bonus_number in my_numbers:
		print("2등")
	elif count == 5:
		print("3등")
	elif count == 4:
		print("4등")
	elif count == 3:
		print("5등")
	else:
		print("꽝")
```



- 컨벤션 = 들여쓰기 하는 것
- 리팩토링 = 코드를 깔끔하게 바꿔서 보기 좋게 하는 것



### 4) 번거롭게 만들기(am_i_lucky2(pick, draw))

```python
#my_numbers랑 real_numbers가 구해지고 사용해야 함
def am_i_lucky2(pick, draw):
	count = 0
	for lucky_number in pick:
		if lucky_number in draw["numbers"]:
			count += 1
	if count == 6:
		return "1등"
	elif count == 5 and draw["bonus"] in pick:
		return "2등"
	elif count == 5:
		return "3등"
	elif count == 4:
		return "4등"
	elif count == 3:
		return "5등"
	else:
		return "꽝"
```

##### 선생님 해설

```python
#draw에 들어가는 게 list고, set로 변경할 경우
def am_i_lucky(pick, draw):
    match = set(pick) & set(draw)
    if len(match) == 6:
        return '1등'
    elif len(match) == 5 and draw["bonus"] in pick:
    elif len(match) == 5:
        return '3등'
    elif len(match) == 4:
        return '4등'
    elif len(match) == 3:
        return '5등'
    else:
        return '꽝'

#draw에 들어가는 게 dict고, set로 변경할 경우
def am_i_lucky(pick, draw):
    match = set(pick) & set(draw['numbers'])
    if len(match) == 6:
        return '1등'
    elif len(match) == 5 and draw["bonus"] in pick:
    elif len(match) == 5:
        return '3등'
    elif len(match) == 4:
        return '4등'
    elif len(match) == 3:
        return '5등'
    else:
        return '꽝'

am_i_lucky(pick_lotto(), get_lotto(837))    
   
list_1 = [1, 2, 3, 4, 5, 6]
dict_1 = {
    'numbers' : [1, 2, 3 ,4, 5, 6],
    'bonus' : 7
}
am_i_lucky(list_1, dict_1)
```



