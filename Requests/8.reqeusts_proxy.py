#coding:utf-8
import requests

url = 'https://www.baidu.com'




proxy = {
    # 'http': 'http://167.71.213.9:3128',
    # 'https': 'https://165.225.88.49:10605',
    # 'https': 'https://177.131.22.186:80',
    'http': 'http://60.191.11.251:3128',
}

response = requests.get(url, proxies=proxy, timeout=2)
print(response.status_code)



