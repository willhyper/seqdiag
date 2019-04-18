import requests
import random
import time


url = 'http://localhost:8000'

while True:
    try:
        requests.post(url, json={"series1": random.random()})
        time.sleep(1)
    except:
        continue