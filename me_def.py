import requests
import json

def get_fox():
    response = requests.get('https://randomfox.ca/floof/')
    json_data = json.loads(response.text)
    return  json_data['image']

def get_anekdot():
    while True:
        try:
            response = requests.get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')
            json_data = json.loads(response.text, strict=False)
            break
        except json.decoder.JSONDecodeError:
            continue

    return json_data['content']

