# 导包
import requests

# 准备url
url = 'http://127.0.0.1:8080/js/data.json'

# 发送请求

response = requests.get(url)
print(response.status_code)
print(response.content.decode())
dict = response.json()
print(type(dict))
print(dict.get('name'))
