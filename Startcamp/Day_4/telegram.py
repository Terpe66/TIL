import requests

MY_CHAT_ID = "663329882"
BOT_TOKEN = "720292980:AAERJD2xWroPoO6hrhoNJjqM1tDiqhbpa3c"
msg = "Ryan"

url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, msg)

response = requests.get(url)
print(response.json())