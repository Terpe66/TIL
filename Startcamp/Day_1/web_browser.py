import webbrowser

keywords = [
    'Captain America', 
    'Ironman', 
    'Hulk', 
    "Thor"
]

for keyword in keywords:
    url = "https://www.google.com/search?q=" + keyword
    webbrowser.open_new(url)