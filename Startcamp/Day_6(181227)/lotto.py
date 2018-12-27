# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
import random
import requests
import threading

def thread(msg1, msg2, msg3, bad = ''):
    MY_CHAT_ID = "663329882"
    BOT_TOKEN = "720292980:AAERJD2xWroPoO6hrhoNJjqM1tDiqhbpa3c"
    requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
    requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
    requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
    if bad != '':
        requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, bad))
        pass
    pass

app = Flask(__name__)

@app.route("/")
def lotto():
    return render_template("lotto.html")
    
@app.route("/lucky")
def lucky():
    MY_CHAT_ID = "663329882"
    BOT_TOKEN = "720292980:AAERJD2xWroPoO6hrhoNJjqM1tDiqhbpa3c"
    
    title = request.args.get("title")
    my_numbers = [int(request.args.get("number1")), int(request.args.get("number2")), int(request.args.get("number3")), int(request.args.get("number4")), int(request.args.get("number5")), int(request.args.get("number6"))]
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(title)
    response = requests.get(url)
    lotto_data = response.json()
    numbers = []
    for key, value in lotto_data.items():
        if "drwtNo" in key:
            numbers.append(value)
    bonus_number = lotto_data["bnusNo"]
    real_numbers = {"numbers" : numbers, "bonus" : bonus_number}
    lucky_numbers = real_numbers["numbers"]
    
    count = 0
    for lucky_number in my_numbers:
        if lucky_number in lucky_numbers:
            count += 1


    if count >= 3:
        if count == 6:
            rank = "1등"
        elif count == 5 and bonus_number in my_numbers:
            rank = "2등"
        elif count == 5:
            rank = "3등"
        elif count == 4:
            rank = "4등"
        elif count == 3:
            rank = "5등"
        msg1 = "{0}회차 로또 당첨 번호는 {1}, 보너스 번호는 {2}입니다.".format(title, sorted(lucky_numbers), bonus_number)
        msg2 = "선택하신 번호는 {0}입니다.".format(my_numbers)
        msg3 = title + "회차 당첨은 {0}입니다.".format(rank)
        threading.Thread(target=thread, args=(msg1, msg2, msg3)).start()
        #send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
        #send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
        return render_template("lucky.html", title = title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = rank)
    else:
        rank = "꽝"
        msg1 = "{0}회차 로또 당첨 번호는 {1}, 보너스 번호는 {2}입니다.".format(title, sorted(lucky_numbers), bonus_number)
        msg2 = "선택하신 번호는 {0}입니다.".format(my_numbers)
        msg3 = title + "회차 당첨은 {0}입니다.".format(rank)
        bad = "돈을 날렸습니다."
        threading.Thread(target=thread, args=(msg1, msg2, msg3, bad)).start()
        # send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
        # send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
        # send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, bad))
        return render_template("lucky.html", title = title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = rank, bad = bad)




    # if count >= 3:
    #     msg1 = title + "회차 로또 당첨 번호는 " + str(sorted(lucky_numbers)) + ", 보너스 번호는 " + str(bonus_number) + "입니다."
    #     msg2 = "나의 번호는 " + str(my_numbers) + "입니다."
    #     if count == 6:
    #         rank = "1등"
    #         msg3 = title + "회차 당첨은 " + rank + "입니다."
    #         send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
    #         send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
    #         send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
    #         return render_template("lucky.html", title = title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = rank)
    #     elif count == 5 and bonus_number in my_numbers:
    #         rank = "2등"
    #         msg3 = title + "회차 당첨은 " + rank + "입니다."
    #         send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
    #         send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
    #         send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
    #         return render_template("lucky.html", title = title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = rank)
    #     elif count == 5:
    #         rank = "3등"
    #         msg3 = title + "회차 당첨은 " + rank + "입니다."
    #         send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
    #         send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
    #         send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
    #         return render_template("lucky.html", title = title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = rank)
    #     elif count == 4:
    #         rank = "4등"
    #         msg3 = title + "회차 당첨은 " + rank + "입니다."
    #         send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
    #         send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
    #         send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
    #         return render_template("lucky.html", title = title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = rank)
    #     elif count == 3:
    #         rank = "5등"
    #         msg3 = title + "회차 당첨은 " + rank + "입니다."
    #         send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
    #         send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
    #         send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
    #         return render_template("lucky.html", title = title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = rank)
    # else:
    #     rank = "꽝"
    #     msg3 = title + "회차 당첨은 " + rank + "입니다."
    #     bad = "돈을 날렸습니다."
    #     send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
    #     send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
    #     send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
    #     send4 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, bad))
    #     return render_template("lucky.html", title = title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = rank, bad = bad)




    
    # if count == 6:
    #     rank = "1등"
    # elif count == 5 and bonus_number in my_numbers:
    #     rank = "2등"
    # elif count == 5:
    #     rank = "3등"
    # elif count == 4:
    #     rank = "4등"
    # elif count == 3:
    #     rank = "5등"
    # else:
    #     rank = "꽝" 
    #     bad = "돈을 날렸습니다."

    # msg1 = title + "회차 로또 당첨 번호는 " + str(sorted(lucky_numbers)) + ", 보너스 번호는 " + str(bonus_number) + "입니다."
    # msg2 = "나의 번호는 " + str(my_numbers) + "입니다."
    # msg3 = title + "회차 당첨은 " + rank + "입니다."

    # send1 = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1)
    # send2 = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2)
    # send3 = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3)
    # send4 = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, bad) 
    

    # def happy():
    #     if count >= 3:
        #     send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
        #     send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
        #     send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
        # print(send1.json(), send2.json(), send3.json())
    # else:
        # send1 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg1))
        # send2 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg2))
        # send3 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg3))
        # send4 = requests.get("https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, bad))
    #     print(send1.json(), send2.json(), send3.json(), send4.json())
        
    
    # print(response3.json())
    
    # if count >= 3:
    #     print(response1.json(), response2.json(), response3.json())
    # else:
    #     print(response1.json(), response2.json(), response3.json(), response4.json())
    
    # if count == 6:
	   # return render_template("lucky.html", title=title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = "1등")
    # elif count == 5 and bonus_number in my_numbers:
    #     return render_template("lucky.html", title=title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = "2등")
    # elif count == 5:
    #     return render_template("lucky.html", title=title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = "3등")
    # elif count == 4:
    #     return render_template("lucky.html", title=title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = "4등")
    # elif count == 3:
    #     return render_template("lucky.html", title=title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = "5등")
    # else:
    #     return render_template("lucky.html", title=title, lucky = sorted(lucky_numbers), bonus = bonus_number, pick = sorted(my_numbers), rank = "꽝", bad = "돈을 날렸습니다.")

    # return render_template("lucky.html", title=title, my_numbers=my_numbers, lucky_numbers=lucky_numbers)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)