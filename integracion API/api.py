import requests

def get_data_from_api(city):
    url =f"https://wttr.in/{city}?format=%T+%t+%c+%C"

    response=requests.get(url)

    return response.text

def take_info():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)
    return response.json()[f"text"]