import re
import requests

def login():

    # url
    url =  'https://passport.csdn.net/v1/register/pc/login/doLogin'

    # session
    session = requests.session()

    # headers
    session.headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4168.2Safari / 537.36'
    }

    # formdata
    fromdata = {
        'loginType': "1",
        'pwdOrVerifyCode': "jxtabc19970220",
        'uaToken': "137#c799hE9oUJFKmu1kAEe8EvzZIn1BsRwqCkzocURpw4ebFo1iY+NeQtCp6TgIlfSwx28WpWHIKv0QiR9vDMzITefcxY2vMA5f+c/eJOA4stit07oZm+O5G4DScrNZgqqBMdsMp92VG3E1i5hAY9RmfkuLH1mEOAMpeMgX8G7iOpVgd+Km4e1tP7vGRSe10LQ8rzs/sp4oSFqqi/W70DlPhoIOfCAXNk7iKIGlfnUwRIiB784+aEQWz5f/0NGScVHS1F0A46OOKEBARXsKLRrAWqhfKmP6HXRN+lm+8VAtrEka4e2o9Qi6VpxllbL1bXMznMbmwCdEtZBFJkwWjqlkxR6lFtskan4MtvqH7rArSs76653SCXNJ2BoLr4Mt8zjOmOat8HRKbq1vUB4hUr5NYp/HoilhTjkId3cnYPvESvD/1yEBjXnt3X/RqF9Iy29FoRhIE7zhYUTfi5CpG/vVf9OF+byUu0s8B+JY1wqb1I3KH6MOw/In4g97odHB39EX9EbMPsXDOeyf6cIz8QMOi9ydXYB4Wi3+RniqzNRcu192UcAA/isxyoQ2oNNdDI1avbC86oJRq7YlZ0Gtw1hp5RqRYp/FZSWQfs0Zgjm+BTWk7c8ADzJbJqrnajBFHm11h++51tdeswaB7PYGeW+mcZays/+ZXmZHlXlwIqYrdTie6aCQAS7d3Gsd1i07pitXE+HHKwzRA47n3c+XKEV7rJzh4VNigKSqpKCkerrhVsdvgg9EdrwH+kBOpr3/U29A7fj53vWLZ50geAm0IaGfYnEStFDX5EONQgqzrHs8lxXwTEQlEGwSgPUEF2CYzuYpLUHFX9hH/X+HAYDFfM9RT1nnd1IPFB7hcCMgRVGNNokXOi28EJC9YMnJH89DFSE4o2V5ncOqn0ZzjVoK4divQDvkyLZdiRc3ShlxSS0YpoDHb26sBUMnp9EQg8WEYTUx1lg5pIV0QeJJNh7pU0OcEIgijXppYTJyT2vlvtpmQonJ+ZDVpRUw1AeiBqWbUmVS1qPkpXicQono+ZDPJ0Uc1Ae7+WIjqS+QTVWnCEjOQofJ+GXppkOm1AEy+pipxTJS1qQypXpcQeno+ZXVpk/m9h0ONfP9iISeQn/vLO7X8y7hH1a1XX5avE3N99SMgdB9R+CqSI8IrotBMhuf7/MDLj7QAPQZpdcWdohCy66Tx3W6iVnWFu4KOzm1izaMhehdyEssjSac0/ewolwDCJolef32H6kgdsxWp0x6lw0/cB5retOWuI+ojJDq0PfRAccGpOR7Kmpr/wut3o335MjXiXIXgt2yERN0u19C0+u/AqNWDpCiPx9cDFomHnCKtAnisPhe6NK9nj8bSzQYRi/Vuc7Fi8Ivie/Cbzz6JUOtaucXMY4T6Q1hQQFrKv6XTGymzdqj7TP/qxEk2IjPKBWNRUKL4E9HXPJEX0AfB0c82oYB+Kuu6Zd8N4K7h563Q0t4lp0/+8sEzU3HJjKBdlcMtEe=",
        'userIdentification': "15737103427"
    }

    # 登录
    session.post(url, data=fromdata)

    # 验证登录
    response = session.get('https://i.csdn.net/#/uc/profile')
    print(response.url)

login()

