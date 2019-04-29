# coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.anjuke.com/sy-city.html')

#   获取热门城市列表
ret1 = driver.find_elements_by_xpath("//div[@class='hot-city']/a")

#   将城市及对应Url放入字典
city_list = {li.text: li.get_attribute('href') for li in ret1}

print(city_list)

time.sleep(3)

driver.quit()
