# coding=utf-8
import requests


class Readfree:

    def __init__(self):
        pass

    def str_to_dic(self, str):  # 使用字典推导式将字符串转化为字典
        return {i.split("=")[0]: i.split("=")[1] for i in str.split("; ")}



if __name__ == '__main__':
    headers = {
        'User-Ageng': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
                        AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    tmp = "OUTFOX_SEARCH_USER_ID_NCOO=57382894.089077; \
    csrftoken=R68atAZPO16JptocHkpI6AQBVlgZIXNWrwOKRW4aiwVQcCe6pvVLgoeWpYqIuuUX; \
    sessionid=9lfqhnqji48gjxforjcobcdopj5ydh4q"

    url = 'https://readfree.me/'

    readfree = Readfree()

    cookies = readfree.str_to_dic(tmp)

    r = requests.get(url, headers=headers, cookies=cookies)

    # with open("readfree.html", 'w', encoding='utf-8') as f:
    #     f.write(r.content.decode())