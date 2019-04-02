# coding=utf-8
"""
    抓取豆瓣读书 - 新书速递 内容并存入Excel
    只进行一次正则匹配拿到数据并存入Excel
"""
import requests
import re
import xlwt

def parsingHtml(baseUrl):
    html = requests.get(baseUrl).text
    # 直接抓取所需信息
    pattern = re.compile(
        '<a class="cover".*?img src="(.*?)"/></a>.*?<a href="(.*?)">(.*?)</a>.*?<span class="font-small.*?">(.*?)</span>.*?<p class="color-gray">(.*?)</p>.*?<p.*?>(.*?)</p>.*?',
        re.S)
    # 解析完成后数据格式为[()]
    bookList = re.findall(pattern, html)

    # 将元组内容去除头尾空格并格式成所需格式
    books = []

    for i, v in enumerate(bookList):
        # if i == 0:
        #     continue

        tmp = []
        for item in v:
            # 去除空格
            new = item.strip()
            if len(new) == 0:
                new = "评价人数不足"
            tmp.append(new)

        books.append(tmp)

    return books

def saveToExcel(infolist):
    """
    将书籍信息写入Excel
    :param infolist: 书籍列表
    :return: 无
    """
    # 新建一个excel
    book = xlwt.Workbook()
    # 添加一个sheet页
    sheet = book.add_sheet("info")
    # 控制行
    row = 0
    # 增加首行
    title = ["图片地址", "详情地址", "书名", "评分", "作者/出版社/出版日期", "书籍简述"]
    infolist.insert(0, title)

    # 写入内容
    for info in infolist:
        print(info)
        # 控制列
        col = 0

        for s in info:
            sheet.write(row, col, s)
            col += 1
        row += 1

    book.save("bookInfo.xls")


url = 'https://book.douban.com/latest?icn=index-latestbook-all'


if __name__ == '__main__':
    info = parsingHtml(url)
    saveToExcel(info)
