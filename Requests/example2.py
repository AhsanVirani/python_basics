import requests

r = requests.get('https://httpbin.org/basic-auth/ahsan/testing', auth=('ahsan', 'testing'), timeout=3)
print(r.text)