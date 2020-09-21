#coding:utf-8
import requests

# url地址中的协议不能缺失
url = "http://www.baidu.com"


headers = {

'Host': 'www.baidu.com',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'BAIDUID=1BEC78D4B8CCE6005F445C9D29314E42:FG=1; PSTM=1564419288; BD_UPN=123253; BIDUPSID=89BE8CB3008263B831ECF0312B98C883; H_WISE_SIDS=114743; MCITY=-271%3A; BDUSS=nQ3UllDQWlUUWRQeEFoTGQ1ZFNtVVRMNWM4M3JYWkw0ZHEzR2VSSkhhSkcyRUJmRVFBQUFBJCQAAAAAAAAAAAEAAACYBMFEZ2%7EG9LPMODg4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEZLGV9GSxlfd; BDUSS_BFESS=nQ3UllDQWlUUWRQeEFoTGQ1ZFNtVVRMNWM4M3JYWkw0ZHEzR2VSSkhhSkcyRUJmRVFBQUFBJCQAAAAAAAAAAAEAAACYBMFEZ2%7EG9LPMODg4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEZLGV9GSxlfd; BDSFRCVID=knCOJeC62xE9zc7rOheOMWn7tmytN1nTH6ao9u4pmKTlhGWn4iwTEG0PDM8g0KubMWQuogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR-qVIK5tIK3H48k-4QEbbQH-UnLq-ba02OZ04n-ah05DpC6Xn5Y0P70bf6L0hcLW20j0h7m3UTdsq76Wh35K5tTQP6rLf6OtJc4KKJxbp5sShOv5t5rDx_AhUJiB5OMBan7_qvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbCD9j6AhjTO0eU5eetjK2CntsJOOaCvzVqROy4oWK441DUnutMRHBG7Qhn5_al3ZDqvoD-Jc3M04X-o9-hvT-54e2p3FBUQFJK_CQft20b0kMbOm2bQaXbrC-R7jWhk2ep72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDqTKOJRkj_Cvt-5rDHJTg5DTjhPrMyG7iWMT-MTryKKOOBC3cql6bhbOqM4u1WfciB5OMBanRhlRNB-3iV-OxDUvnyxAZXlAHtfQxtNRJKRnm0b7hHxA4LqoobUPUDMJ9LUkqW2cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD-abK8mjjL3MbLfbHAOetJyaR3rKDnvWJ5TMCoGLtOpLT-XXtJvt4QBamvkWCKK2bjGShPC-tn6jMFr3H_H-PoZ2n6HoDb63l02Vb5ae-t2ynLVMMQgtPRMW238oq7mWITUsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCKj53bDN8DJ6nfb5kXQbnV-nT_JRnG-tTs5t_HqxbXq-nX02OZ0l8Kttnpbtcnjn5cM-LgXJJXtb3LM6nwoRrmWIQHDITGjb3Vyp0jM-JU2j30ban4KKJx3pCWeIJo5t5Y3p_0hUJiBM7MBan7-lRIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbRO4-TFKejbBjfK; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=1; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; COOKIE_SESSION=16145_1_7_6_14_51_0_4_6_7_0_2_1535305_0_42_0_1600414279_1598324637_1600414237%7C9%23673515_16_1598324633%7C9; H_PS_PSSID=32617_1459_32737_7543_32327_31253_32723_7606_32117_32718; H_PS_645EC=df3942rM6MrAEI8W%2BfCfahLr8f0%2BwTuYDPQieqfCSyPqWJrznKRAUhC%2Fk2g; sugstore=1',
}
response1 = requests.get(url,headers=headers)
print(response1.status_code)
print(response1.request.headers)
print(len(response1.content))
with open('baidu2.png','wb') as f:
    f.write(response1.content)


#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
# }
# response2 = requests.get(url)
#
#
# print(response2.request.headers)
# print(len(response2.content))