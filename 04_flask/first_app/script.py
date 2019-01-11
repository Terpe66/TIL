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
