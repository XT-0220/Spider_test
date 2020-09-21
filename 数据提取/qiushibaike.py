import requests
from lxml import etree


class QiuBai(object):
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/text/page/1'
        self.headers = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4168.2Safari / 537.36'
        }
    def get_data(self,url):
        '''
        发送请求
        :param url:
        :return:
        '''
        response = requests.get(url,headers=self.headers)
        return response.request

    def parse_data(self,data):
        '''
        解析响应数据
        :param data:
        :return:
        '''
        html = etree.HTML(data)
        # 先分组 再提取
        div_ele = html.xpath("//div[@class='col1 old-style-col1']")
        print(div_ele)

    def run(self,data):
        # 实现主要逻辑
        # 1.url
        url = self.url
        # 2.发送请求,获取响应
        data = self.get_data()
        # 3.解析响应数据
        # 4.保存数据
        pass

if __name__ == '__main__':
    QiuBai.run()