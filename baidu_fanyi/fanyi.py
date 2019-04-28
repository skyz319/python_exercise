# coding=utf-8
import requests


class Fanyi:
    def __init__(self, keyword):
        # self.header = {
        #     'User-Ageng': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36\
        #      (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        self.header = {
            'User-Ageng':        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
                    AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

        self.data = {
            'from': 'zh',
            'to': 'en',
            'query': keyword,
            # 'transtype': 'translang',
            # 'simple_means_flag': '3',
            # 'sign': '669338.972203',
            # 'token': '5501eff1db41e9e494f387bcc2285a69',
        }

        self.post_url = 'https://fanyi.baidu.com/basetrans'

    def run(self):
        r = requests.post(self.post_url, headers=self.header, data=self.data)
        print(r.status_code)
        print(r.content.decode())


if __name__ == '__main__':
    fanyi = Fanyi("人生苦短，我用Python")
    fanyi.run()
