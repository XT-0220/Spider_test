# 导包
import requests

# 准备url
url = 'https://tieba.baidu.com/p/6852355988'

# 发送请求
response = requests.get(url)
# response.encoding = 'utf8'
# print(response.text)
# 查看响应url
print(response.url)
# 查看响应状态码
print(response.status_code)
# 查看响应头
print(response.headers)
print(response.cookies)
# 查看请求头
print(response.request.headers)
print(response.content.decode())
# response.json()


with open('./picture','wb') as f:
    f.write(response.content.decode())