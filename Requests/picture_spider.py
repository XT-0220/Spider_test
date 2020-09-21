# 导包
import requests

# 准备url
url = 'http://tiebapic.baidu.com/forum/w%3D580/sign=249d5eb8b644ad342ebf878fe0a30c08/14e39f3df8dcd1000f1f0474658b4710b8122f8c.jpg'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.2 Safari/537.36'}
# 发送请求
response = requests.get(url)

print(response.text)
print(response.request.headers)
with open('picture,jpg','wb') as f:
    f.write(response.content.decode())