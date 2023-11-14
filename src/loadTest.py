import requests

for i in range(5000):
    response=requests.get('https://deathdater.pythonanywhere.com/search')
    print(response.status_code)
    print(response.content)