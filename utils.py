import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    try:
        r = requests.get(url, timeout=5)
        return r.json()["content"]
    except:
        return "No quote today 😅"
