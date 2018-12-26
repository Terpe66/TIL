# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import random
import requests
from lucky_number import lucky

app = Flask(__name__)

@app.route("/ping")
def ping():
	return render_template("ping.html")

@app.route("/pong")
def pong():
	ssum = request.args.get("ssum")
	me = request.args.get("me")
	result = me + "=>" + ssum
	match_point = random.choice(range(1, 100))
	
	MY_CHAT_ID = "663329882"
	BOT_TOKEN = "720292980:AAERJD2xWroPoO6hrhoNJjqM1tDiqhbpa3c"
	msg = result
	
	url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg)
	
	response = requests.get(url)
	print(response.json())


	return render_template("pong.html", match_point=match_point, ssum=ssum)



@app.route("/<string:username>/<string:workspace>")
def username_workspace(username, workspace):
    return render_template(
        "ide.html", 
        name = username, 
        space = workspace)

# @app.route("/")
# # route는 주소창에 들어오는 값
# def index():
#     lunch = random.choice(["20층", "Diet"])
#     return render_template("index.html", menu = lunch)

@app.route("/")
def index():
    return render_template("test.html")

    
@app.route("/hi")
def hi():
    return "Hello SSAFY"

@app.route("/pick_lotto")
def pick_lotto():
    return jsonify(random.sample(range(1, 46), 6))
 
    
@app.route("/get_lotto/<int:draw_no>")
def get_lotto(draw_no):

    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(draw_no)
    
    response = requests.get(url)
    lotto_data = response.json()
    
    numbers = []
    for key, value in lotto_data.items():
        if "drwtNo" in key:
            numbers.append(value)
    bonus_number = lotto_data["bnusNo"]
    real_numbers = {"numbers" : numbers, "bonus" : bonus_number}
    
    return jsonify(real_numbers)


@app.route("/lucky/<int:draw_no>/<int:a>,<int:b>,<int:c>,<int:d>,<int:e>,<int:f>")
def lotto(draw_no, a, b, c, d, e, f):
    result = lucky(draw_no, a, b, c, d, e, f)
    return result


# def lucky(draw_no, a, b, c, d, e, f):
# 	my_numbers = [a, b, c, d, e, f]

# 	url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(draw_no)
# 	response = requests.get(url)
# 	lotto_data = response.json()
# 	numbers = []
# 	for key, value in lotto_data.items():
# 		if 'drwtNo' in key:
# 			numbers.append(value)
# 	bonus_number = lotto_data['bnusNo']
# 	real_numbers = {"numbers" : numbers, "bonus" : bonus_number}


# 	count = 0
# 	for lucky_number in my_numbers:
# 		if lucky_number in real_numbers["numbers"]:
# 			count += 1
# 	if count == 6:
# 	    return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "1등")
# 	   # "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 1등입니다."
# 	elif count == 5 and bonus_number in my_numbers:
# 		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "2등")
# 		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 2등입니다."
# 	elif count == 5:
# 		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "3등")
# 		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 3등입니다."
# 	elif count == 4:
# 		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "4등")
# 		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 4등입니다."
# 	elif count == 3:
# 		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "5등")
# 		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 5등입니다."
# 	else:
# 		return render_template("test.html", real = sorted(real_numbers["numbers"]), pick = sorted(my_numbers), rank = "꽝", bad = "돈을 날렸습니다.")
# 		# "당첨 번호는 " + str(real_numbers["numbers"]) + "이고, 내 번호는 " + str(my_numbers) + "이며 돈을 하늘에 뿌렸습니다."



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)


# @app.route("/send_message")
# def send_message():
#     telgram.send('msg')
#     return telgram