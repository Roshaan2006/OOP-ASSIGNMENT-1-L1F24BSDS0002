import requests

def fetch(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url=  "https://www.timesofpakistan.com/"

fetch(url, "G:/C++/times.html")