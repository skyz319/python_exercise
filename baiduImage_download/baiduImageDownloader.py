# coding=utf-8
"""根据关键字下载百度图片"""
import re
import os
import urllib
import requests


def getPage(keyword, page, n):
    """
    拼接Page的请求URL
    :param keyword: 关键词
    :param page: 页码
    :param n: 页码
    :return: 拼接后的URL
    """
    page = page * n
    keyword = urllib.parse.quote(keyword, safe="/")
    baseUrl = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = baseUrl + keyword + "&pn=" + \
        str(page) + "&gsm=" + str(hex(page)) + \
        "&ct=&ic=0&lm=-1&width=0&height=0"
    return url


def get_onepage_urls(onePageurl):
    """å
    根据URL地址得到图片地址
    :param onePageurl:
    :return: 图片地址
    """
    try:
        html = requests.get(onePageurl).text
    except Exception as e:
        print("error: -> ", e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    return pic_urls


def down_pic(pic_urls):
    """根据给定图片url下载所有图片"""
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            # 存储于当前目录下
            # string = str(i+1)+'.jpg'

            # 存储至关键字目录下
            string = file + r'//' + keyword + '_' + str(i) + '.jpg'
            with open(string, 'wb') as f:
                f.write(pic.content)
                print("成功下载第%s张图片: %s" % (str(i + 1), str(pic_url)))
        except Exception as e:
            print("下载第%s张图片失败： %s" % (str(i + 1), str(pic_url)))
            print(e)
            continue


if __name__ == '__main__':

    keyword = input("请输入关键词：")
    page_begin = 0
    page_number = 30
    image_number = 3
    all_pic_urls = []

    file = keyword
    y = os.path.exists(file)
    if y == 1:
        print('目录已存在，请输入文件夹名!')
        file = input('文件夹名：')
        os.mkdir(file)
    else:
        os.mkdir(file)

    while 1:
        if page_begin > image_number:
            break
        print("第%d将请求数据", [page_begin])
        url = getPage(keyword, page_begin, page_number)
        onepage_urls = get_onepage_urls(url)
        page_begin += 1

        all_pic_urls.extend(onepage_urls)

    down_pic(list(set(all_pic_urls)))
