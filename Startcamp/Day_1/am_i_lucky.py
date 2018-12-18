import requests
import random

url = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"

response = requests.get(url, verify = False)
data = response.json()

real_numbers = []

for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_number = data['bnusNo']
print(real_numbers)

numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)
my_numbers.sort()

print(my_numbers)

# my_numbers, real_numbers, bonus_number
# 1등 : my_numbers == real_numbers
# 2등 : real_numbers 와 my_numbers가 5개 같고 my의 나머지 하나가 bonus_number
# 3등 : real_numbers 와 my_numbers가 5개 같다
# 4등 : real_numbers 와 my_numbers가 4개 같다
# 5등 : real_numbers 와 my_numbers가 3개 같다
# 꽝

check_numbers = []
n = 0
for key in my_numbers:
        if my_numbers[n] == real_numbers[0]:
                check_numbers.append(my_numbers[n])
        elif my_numbers[n] == real_numbers[1]:
                check_numbers.append(my_numbers[n])
        elif my_numbers[n] == real_numbers[2]:
                check_numbers.append(my_numbers[n])
        elif my_numbers[n] == real_numbers[3]:
                check_numbers.append(my_numbers[n])
        elif my_numbers[n] == real_numbers[4]:
                check_numbers.append(my_numbers[n])
        elif my_numbers[n] == real_numbers[5]:
                check_numbers.append(my_numbers[n])
        elif my_numbers[n] == bonus_number:
                check_numbers.append(my_numbers[n])
        n += 1

if len(check_numbers) = 6