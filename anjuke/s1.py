import requests
from bs4 import BeautifulSoup

response = requests.get(
    url='https://www.anjuke.com/sy-city.html'
    # url='https://www.autohome.com.cn/all/'
)
# 使用网页返回的charset进行编码 response.apparent_encoding
response.encoding = response.apparent_encoding
# print(response.text)

# 将Html转换为BeautifulSoup对象。 features 以什么方式进行转换
soup = BeautifulSoup(response.content, features='html.parser')


target = soup.find(arrts={'class': 'hot-city'})

print(target)

