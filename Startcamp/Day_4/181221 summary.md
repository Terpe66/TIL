# 181221 수업정리

## 1. 검색한 거 필기(vscode 터미널 bash)

1번은 꼭 하지 않아도 됨.
git 연동? 할 때 필요한 부분인듯
기본 power shell에서도 git 연동 빼면 같나봄.
```
파일> 환경 설정> 설정 (Ctrl +,)

오른쪽 창에 {} 안에 붙여 넣기 :

"terminal.integrated.shell.windows": "C:\\WINDOWS\\System32\\bash.exe"
# 이거 안 됨

(여기서 원하는 다른 사용자 정의 설정을 넣을 수 있습니다)

해당 경로를 체크 아웃하여 bash.exe 파일이 있는지 확인하십시오. 그렇지 않으면 경로가있는 곳을 찾아 대신 해당 경로를 가리 킵니다.

지금 VS 코드의 터미널 창을 닫고 다시 시작하면 PowerShell 대신 bash가 열립니다.
```



## 2. 주소 구분(https://ide.c9.io/terpe66/startcamp)

### 1) https://

### 2) ide.c9.io : 도메인

### 3) /terpe66/startcamp : route(라우트)



## 3. flask(내일 다시 확인)

### 1) run 쉽게 하기

```python
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    
# 제일 하단에 써야 함
```

### 2) html을 리턴

```python
@app.route("/")
# route는 주소창에 들어오는 값
def index():
    lunch = random.choice(["20층", "Diet"])
    return render_template("index.html", menu = lunch)
```

#### 2-1) index.html

```html
<h1>Hi</h1>
<h2>Lunch: {{ menu }}</h2>

<p>
    집에 보내줘
</p>
```

### 3) 연습(로또 회차, 내 번호 입력 후 당첨 확인하기)

```python
@app.route("/lucky/<int:draw_no>/<int:a>,<int:b>,<int:c>,<int:d>,<int:e>,<int:f>")
# def lotto(draw_no, a, b, c, d, e, f):
#     result = lucky(draw_no, a, b, c, d, e, f)
#     return jsonify(result)
def lucky(draw_no, a, b, c, d, e, f):
	my_numbers = [a, b, c, d, e, f]

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
	    return "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 1등입니다."
	elif count == 5 and bonus_number in my_numbers:
		return "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 2등입니다."
	elif count == 5:
		return "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 3등입니다."
	elif count == 4:
		return "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 4등입니다."
	elif count == 3:
		return "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 5등입니다."
	else:
		return "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 돈을 하늘에 뿌렸습니다."
```

### 3-1) 로또 페이지 수정(function.py + html 활용)

```python
#route 설정
@app.route("/lucky/<int:draw_no>/<int:a>,<int:b>,<int:c>,<int:d>,<int:e>,<int:f>")
def lotto(draw_no, a, b, c, d, e, f):
    result = lucky(draw_no, a, b, c, d, e, f)
    return result
```

```python
#function.py 설정

# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template
import random
import requests

def lucky(draw_no, a, b, c, d, e, f):
	my_numbers = [a, b, c, d, e, f]

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
	    return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "1등")
	   # "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 1등입니다."
	elif count == 5 and bonus_number in my_numbers:
		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "2등")
		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 2등입니다."
	elif count == 5:
		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "3등")
		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 3등입니다."
	elif count == 4:
		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "4등")
		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 4등입니다."
	elif count == 3:
		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "5등")
		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 5등입니다."
	else:
		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "꽝", bad = "돈을 날렸습니다.")
		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 돈을 하늘에 뿌렸습니다."

```



## 4. input, output

### 1) html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>ping</title>
</head>
    <body>
        <form>
            <input type="text" name="" placeholder="숫자를 써라"/>
            <input type="color" />
            <input type="submit" value="펑!" />
        </form>
    </body>
</html>
```

```python
# ! + tab을 누르면 기본 입력 해줌. DOCTYPE ~ </html>까지
# input은 입력창
# input type text:텍스트, color:색 선택, submit:제출, email:이메일, date:날짜
# placeholder는 입력창의 안내? 글, value는 보이는 메시지
```



## 5. chat bot

```json
// 20181221163209
// https://api.telegram.org/bot720292980:AAERJD2xWroPoO6hrhoNJjqM1tDiqhbpa3c/getUpdates

{
  "ok": true,
  "result": [
    {
      "update_id": 306369617,
      "message": {
        "message_id": 1,
        "from": {
          "id": 663329882,
            # 이게 내 계정
          "is_bot": false,
          "first_name": "원진",
          "last_name": "이"
        },
        "chat": {
          "id": 663329882,
          "first_name": "원진",
          "last_name": "이",
          "type": "private"
        },
        "date": 1545377443,
        "text": "/start",
        "entities": [
          {
            "offset": 0,
            "length": 6,
            "type": "bot_command"
          }
        ]
      }
    }
  ]
}
```



# 6. 기억할 것

C, python 차이 (ex. for)

class 안에 있는 title 등 빼는 것