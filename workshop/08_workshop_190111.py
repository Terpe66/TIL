import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/dictionary/<string:word>")
def dictionary(word):
    words = {
        "apple":"사과",
        "orange":"오렌지",
        "ant":"지또니",
        "doll":"성령"
    }

    if word in words:
        return f"{word}은/는 {words[word]}입니다!"
    else:
        return f"{word}은/는 나만의 단어장에 없는 단어입니다!"


if __name__ == "__main__":
    app.run(debug=True)