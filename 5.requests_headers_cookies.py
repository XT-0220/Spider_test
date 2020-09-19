#coding:utf-8
import requests

url = 'https://github.com/exile-morganna'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Cookie': '_ga=GA1.2.2020081379.1564843409; _octo=GH1.1.943957167.1564843409; _device_id=2b9b2f9ea7514ebb13aeea375da7086f; tz=Asia%2FShanghai; tz=Asia%2FShanghai; _gat=1; has_recent_activity=1; user_session=9cB9MrQvvalXGiscSAgFTPX_hU2xX4kKj6hVrbiGrJY0mUBh; __Host-user_session_same_site=9cB9MrQvvalXGiscSAgFTPX_hU2xX4kKj6hVrbiGrJY0mUBh; logged_in=yes; dotcom_user=xiaozhisummer; _gh_sess=C6lNC8jmNS2wrDynTDjGBbi1miWWSudbhUfELWFT3u1hc0IPPacfL7uNzfmUjLDcj10dl24%2BEZP%2Bg%2Fe2gQNHlJzxZIq6%2FnFc0eE8xj6E9clt24tVoEnmOHFCtKfBs5nvnWS3nirxK6TBDljDICdafQKDtrkovBDFGO3VJj%2BjR3wmjIfCCQidA2jFZOTfo3kYa0nMrNmqT2XyMfD7TCzwC88eN0LYonVXwnxScn0old00Upu7jvBfpAETYvp4dF0Vm8PkLEJWbH8NOu1i3pSv1WRZN0VltQkQixCwL3MpqV0d8qi4xXnJ5rUamfqSDFI2NNYiB0K4vcjZPAKBD5XvvOhA4W3necqB69mED3aqucL%2FC0BMEQtmbquoGEnqE28JSGlXk5hHMzMiYeQ5F%2Fan2Ln7ZjTy1mlU5ch2FmyrckHkzpFDkJJZdPWHxvjIbCVcxHBRxqvrNDsFT0kD1%2B5XClFlTVCBTWSi8OBvdGDjyArBqO6fvz80wg8DPgPERtI3l%2FPgqSLkDVb4fbOkMUzTRn%2Bq3EKJCLuuTTPqTQDxzWW7iOJ41vbhsXmxkN3yTMmYPlHAq5lulF4L%2FgD3aM%2FKUImEBG9QvZgX6SOGdn%2B1ObyaPFzjyuYX05W0zq42nqZZ4jFEf25xzonS3bKYn2rIy97lykmrewRu7Zv%2Bglb6clwTe6CSFA2LfiuzmYGdaWkhcEisl3TyRb%2B6febgZfJq2HcGxQKhZRBCYm%2BXJfl6XvPhqQyQomnFL%2BpBYrwZCrqnCTlcICsFQhbGCL4T64wnK92%2BpXDIxBLOw0lmDez8byii90s5OPnkUovBuF43ktVJHV5ps8D2nCM%3D--fABmaRquxiAf8%2Bvt--7iVBYvTj914D3NsT6QxMig%3D%3D'
}

response = requests.get(url, headers=headers)

print(response.url)
with open('github_with_cookies.html', 'wb')as f:
    f.write(response.content)