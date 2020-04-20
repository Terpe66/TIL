import requests

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"

response = requests.get(url)
num_data = response.json()

nums = []
for key, value in num_data.items():
    if "drwtNo" in key:
        nums.append(value)

print(nums)
