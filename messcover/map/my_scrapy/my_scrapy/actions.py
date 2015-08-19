import requests

def start_url():
    r = requests.get('http://localhost:8001/api/')
    local_dict = r.json()

    return str(local_dict[0]['start_url'])
