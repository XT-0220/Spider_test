# 导包
import requests

# 准备url
url = 'https://github.com/XT-0220'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.2 Safari/537.36',
'Cookie': '_octo=GH1.1.2013892943.1580975053; _ga=GA1.2.793530841.1581947398; experiment:homepage_signup_flow=eyJ2ZXJzaW9uIjoiMSIsInJvbGxPdXRQbGFjZW1lbnQiOjYuMTk1ODA5ODEwMDAyMjkxLCJzdWJncm91cCI6ImVtYWlsIiwiY3JlYXRlZEF0IjoiMjAyMC0wMy0wMVQwMToyOTo1OC41MzJaIiwidXBkYXRlZEF0IjoiMjAyMC0wMy0wMVQwMToyOTo1OC41MzJaIn0=; _device_id=f9e77c398e236907eae0e4cae54074d6; user_session=epysr6yYPloxloo8Gf-62HFoG9j9KDddC3PkpeVXRX89tb7a; __Host-user_session_same_site=epysr6yYPloxloo8Gf-62HFoG9j9KDddC3PkpeVXRX89tb7a; logged_in=yes; dotcom_user=XT-0220; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1; _gh_sess=lJbHpUNWYxO5tf0LN47JvrWA%2BoCTeOYqfaqkGLZO8vfNPR2duRuVEJKip9%2Fd8UqYwZQoJgwObQL6Vkz%2BUOdMKxXbFxCeeu7QLn%2BYzgZZKlJUC1dUmuEVKoXrH7hSI75EXNA3Lmi40cZsnywxxLDnqgaH6Xs0DDHlj%2Fo8pzRl5dKPoE02MjQyW0i%2BlHr%2B5gtvNj72ucPBQ4daSg9OGjNVhhvGqIXB1g7I03WTBXmWiwXUZ0ia3ArPdMfIhoSDDjIv42B1Zhd0pFxlu7RGen%2FhVBPWaQgbijFLofJzoFc%2BNs6oBs%2FssKjje4KS9bXAkZTIeqEk2hlvW%2BqI6lZvrwGq5Fu%2BqQaHHTjogxmn5cZyps5EEt3aLzYnNSn6dWiDH0Zm8Mj5fSvI18YvVUxwtWTjyZS%2BsxMsC%2FPIVz4W2%2BPFtVUGjaRbYz7q%2BmeOf9S1%2FuHRfNo8h2aGeNcd1epSYm%2FrBLq%2B9zi1Lrd%2FExtxlkobWEP7onKBew2Ah2km%2Bi5bFzn1I%2BCfsxuq62%2FJk9UxhameqC0mumsABeJVe4eyTNXY%2FRDAzD23zhFn3p49BXpN9DOHEw2n0S%2B11vuC3LIgYwBcnL9pp3%2FI%2B3tspJAY9kpy0n5taHVW84maszRLLqEFTt0WSQCXnfpyXMDtAh7Rr0BNEQum5lm4ACvAmEFZ8On5S4t5ivU1I61Wyoy3vQL3yoFKVfQBk%2FOVOAep%2Fz6sVJY3HJ%2B7C%2FYviOFZYJXjyCq9XoPjaTVFToCDRHlmpCXB7ZXLi%2B31f9Q334hH%2F0t4zajsDluhg36bc6ZYLaGd%2Fa7bmEzcSeH3%2FlMMu1ITrVLoTh3%2FhfnMmEt8vdY6uwtwOgt%2Bb%2BZiyDcIvvR7--8ArkqSD3WhHTbvk0--ie1K9H6pn8KQO5M1xpA%2Buw%3D%3D'
}

response = requests.get(url, headers=headers)
with open('github.html', 'wb') as f:
    f.write(response.content)