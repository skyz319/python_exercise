# coding=utf-8

import requests
import time

class FindProxy:
    def __init__(self):
        self.getUrl = 'https://proxy.mimvp.com/freesecret.php'
        self.header = {
            'User-Ageng': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
                            AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

    def get_proxy(self):
        resp = requests.get(self.getUrl, headers=self.header)
        print(resp.content.decode())

        file_path = '{}.html'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(resp.content.decode())


if __name__ == '__main__':
    findProxy = FindProxy()
    findProxy.get_proxy()