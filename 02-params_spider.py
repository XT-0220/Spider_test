# import requests
#
# url = 'https://www.baidu.com/s?wd=python'
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.2 Safari/537.36'
# }
#
# response = requests.get(url,headers)
# # print(response.content.decode())
# with open('baidu.html','w') as f:
#     f.write(response.content.decode())


import requests

url = 'https://www.baidu.com/s?'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.2 Safari/537.36'
}

kw = {'wd': 'python'}

response = requests.get(url, headers=headers, params=kw)

# print(response.content.decode())
with open('baidu.html','wb') as f:
    f.write(response.content)