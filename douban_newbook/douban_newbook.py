# coding=utf-8
"""
    抓取豆瓣读书 - 新书速递 内容并存入Excel
"""
import requests
import re
import xlwt

def parsingHtml(baseUrl):
    html = requests.get(baseUrl).text
    # 抓取<li></li>中的书籍信息
    pattern = re.compile('<li>(.*?)</li>', re.S)
    bookList = re.findall(pattern, html)

    return bookList

def parsingBooks(infoList):
    print("infoList:", len(infoList))
    # 将书籍列表中数据进行二次匹配,取出左右两列展示的所有书籍信息
    pat = re.compile(
        '<a.*?img src="(.*?)"/></a>.*?<a href="(.*?)">(.*?)</a>.*?<span class="font-small.*?">(.*?)</span>.*?<p class="color-gray">(.*?)</p>.*?<p.*?>(.*?)</p>.*?',
        re.S)
    bookInfoList = []
    for i, v in enumerate(infoList):
        # 解析结果为元组
        bookInfo = re.findall(pat, infoList[i])

        if len(bookInfo) == 0:
            print("bookinfo is zero")
            continue

        # 将元组转为list
        bookInfo = list(bookInfo[0])

        # 清除元素前后空格并格式化无评价的书籍
        for index, item in enumerate(bookInfo):
            new = item.strip()
            if len(new) == 0:
                # 代表豆瓣未提供书籍评分
                new = "评价人数不足"
            bookInfo[index] = new

        bookInfoList.append(bookInfo)

    return bookInfoList

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
    allBook = parsingBooks(info)
    saveToExcel(allBook)
