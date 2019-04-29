# coding=utf-8

from selenium import webdriver
import time

# 实例化一个浏览器
driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()

# 发送请求
driver.get("http://www.baidu.com")

# 设置Window大小
# driver.set_window_size(1920, 1080)
# 最大化窗口
# driver.maximize_window()
# 全屏窗口
# driver.fullscreen_window()

# 元素定位 并 输入内容
driver.find_element_by_id("kw").send_keys("python")

# 元素定位并找到src属性
# driver.find_element_by_id("kw").get_attribute("src")

driver.find_element_by_id("su").click()

# 页面截屏
# driver.save_screenshot('./screenshot.png')

# 获取cookie
cookie = driver.get_cookies()
print(cookie)

print("*" * 500)

# 字典推导式 转换cookies为request模块使用的字典
cookies = {i["name"]: i["value"] for i in cookie}
print(cookies)

print("*" * 500)

# 获取html字符串
source = driver.page_source  # 是浏览器中elements的内容，已加载js、css等

time.sleep(3)

# 退出浏览器
driver.quit()

# 退出当前页面
# driver.close()
