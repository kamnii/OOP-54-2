"""
Эта библиотека нужна для того, чтобы делать HTTP запросы к веб-сайтам и API.
Код снизу делает HTTP GET-запрос и выводит статус ответа.
"""

import requests

headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json'}
response = requests.get('http://httpbin.org/get', headers=headers)
print(response.status_code)

