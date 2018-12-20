import requests
import random

# 선생님 답안
# count = 0
# for my_number in my_numbers:
#     for real_number in real_numbers:
#         if my_number == real_number:
#             count += 1

# print(count)

def pick_lotto():
    # numbers = random.sample(range(1, 46))
    numbers = random.sample(range(1, 46), 6)
# range는 정수 리스트로 뽑음, 위는 list(range(1, 46))으로 안 써도 됨
    return numbers
# sotred()는 반환을 하고, .sort()는 반환하지 않음

my_numbers = pick_lotto()

def get_lotto(draw_no):
    
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(draw_no)
    response = requests.get(url)
    lotto_data = response.json()
    
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    
    bonus_number = lotto_data['bnusNo']
    return {"numbers" : numbers, "bonus" : bonus_number}
    
    real_numbers = get_lotto(draw_no)

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



def am_i_lucky(draw_no):
	my_numbers = random.sample(range(1, 46), 6)

	url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(draw_no)
	response = requests.get(url)
	lotto_data = response.json()
	numbers = []
	for key, value in lotto_data.items():
		if 'drwtNo' in key:
			numbers.append(value)
	bonus_number = lotto_data['bnusNo']
	real_numbers = {"numbers" : numbers, "bonus" : bonus_number}

	count = 0
	for lucky_number in my_numbers:
		if lucky_number in real_numbers["numbers"]:
			count += 1
	if count == 6:
		return "1등"
	elif count == 5 and bonus_number in my_numbers:
		return "2등"
	elif count == 5:
		return "3등"
	elif count == 4:
		return "4등"
	elif count == 3:
		return "5등"
	else:
		return "꽝"