import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/") # ~는 홈, /는 루트, 근데 루트면 최하단 아닌가
def index():
    return "Hi"

@app.route("/ssafy") # 라우트명이랑 함수명은 보통 같게 만들어줌
def ssafy():
    return "SSSSSSafy"

@app.route("/hi/<string:name>")
def hi(name):
    return f"hi. {name}"

@app.route("/dictionary/<string:word>")
def dictionary(word):
    words = {
        "apple":"사과",
        "orange":"오렌지",
        "ant":"지또니",
        "doll":"성령"
    }

    if word in words:
        return f"{word}은/는 words[word]!"
    else:
        return f"{word}은/는 나만의 단어장에 없는 단어입니다!"










# @app.route("/pick_lotto")
# def pick_lotto():
#     return jsonify(random.sample(range(1, 46), 6))

# @app.route("/get_lotto/<int:draw_no>")
# def get_lotto(draw_no):

#     url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(draw_no)
    
#     response = requests.get(url)
#     lotto_data = response.json()
    
#     numbers = []
#     for key, value in lotto_data.items():
#         if "drwtNo" in key:
#             numbers.append(value)
#     bonus_number = lotto_data["bnusNo"]
#     real_numbers = {"numbers" : numbers, "bonus" : bonus_number}
    
#     return jsonify(real_numbers)


# @app.route("/lucky/<int:draw_no>/<int:a>,<int:b>,<int:c>,<int:d>,<int:e>,<int:f>")
# def lotto(draw_no, a, b, c, d, e, f):
#     result = lucky(draw_no, a, b, c, d, e, f)
#     return result







if __name__ == "__main__":
    app.run(debug=True)



# export ??????? = ???????는 alias 같은 느낌인데, 컴퓨터 전역에서 사용하는 환경 변수를 설정함. export ???????? = 로 끝내면 삭제됨
# alias는 소문자도 되는데 export는 $ + 대문자만 써야 해서 불편



# class Flask:
#     def run(self, **kwargs):


    # print("__name__ is __main__")
    



# class Flask:
#    __init__(some_name):