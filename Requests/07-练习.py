import json
import sys
import requests


class baidu(object):

    def __init__(self,word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers = {
            'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4168.2Safari / 537.36'
        }
        self.formdata = {
            'f': 'auto',
            't': 'auto',
            'w': word
        }

    def get_data(self):
        response = requests.post(self.url,headers = self.headers, data=self.formdata)
        return response.content

    def parse_data(self,data):
        dict_data = json.loads(data)
        try:
            print(dict_data['content']['out'])
        except:
            print(dict_data['content']['word_mean'][0])

    def run(self):

        # 流程
        # url
        # 发送请求获取响应
        data = self.get_data()
        # 解析响应
        self.parse_data(data)
        # 保存数据



if __name__ == '__main__':
    # word = input("请输入:")
    word = sys.argv[1]
    baidu = baidu(word)
    baidu.run()