# coding=utf-8
import requests


class TiebaSpider:
    def __init__(self, tieba_name, max_page_num):
        self.tieba_name = tieba_name
        self.max_page_num = max_page_num
        self.url_temp = 'http://tieba.baidu.com/f?kw=' + tieba_name + '&ie=utf-8&pn={}'
        self.header = {'User-Ageng': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

    def get_url_list(self):    # 构造Url列表
        # 贴吧PageNum是i * 50格式
        return [self.url_temp.format(i * 50) for i in range(self.max_page_num)]
        # 等同于下面
        # for i in range(self.max_page_num):
        #     url_list.append(self.url_temp.format(i * 50))
        #


    def paser_url(self, url):   # 发送请求，获取响应

        print(url)
        response = requests.get(url=url, headers=self.header)

        return response.content.decode()

    def save_html(self, html_str, page_num):  # 保存html到文件

        file_path = "{} - 第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url_list()

        for url in url_list:
            html_str = self.paser_url(url)

            page_num = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("AMD", 10)
    tieba_spider.run()

