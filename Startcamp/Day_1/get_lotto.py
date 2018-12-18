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

real_numbers.sort()
bonus_number = data['bnusNo']
print(real_numbers)






# real_numbers = [
#     data['drwtNo1'],
#     data['drwtNo2'],
#     data['drwtNo3'],
#     data['drwtNo4'],
#     data['drwtNo5'],
#     data['drwtNo6'],
#     data['bnusNo']
# ]

# print(real_numbers)

# {
#     "drwtNo1":2,
#     "drwtNo2":25,
#     "drwtNo3":28,
#     "drwtNo4":30,
#     "drwtNo5":33,
#     "drwtNo6":45,
#     "bnusNo":6
# }

