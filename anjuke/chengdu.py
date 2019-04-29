from selenium import webdriver


get_url = 'https://chengdu.anjuke.com/sale/xq1/'

driver = webdriver.Chrome()

driver.get(get_url)

ret1 = driver.find_elements_by_xpath("//ul[@id='houselist-mod-new']/li")

for li in ret1:

    # 房屋图片Url
    # print(li.find_element_by_xpath('.//img').get_attribute('src'))
    #   房屋title
    # print(li.find_element_by_xpath(".//div[@class='house-details']//a").get_attribute('title'))

    # 房屋基本信息
    # ret2 = li.find_elements_by_xpath(".//div[@class='details-item']//span")
    #
    # i = 0
    # for li2 in ret2:
    #     if i == 4:  #   跳过中介名称
    #         continue
    #
    #     print(li2.text)
    #
    #     i += 1
    #
    # print("-" * 10)

    # TODO 有返回为空的情况，需要排除
    # 附近学校信息
    # print(li.find_element_by_xpath(".//span[@class='item-tags tag-school']").text)

    # 房屋总价
    # print(li.find_element_by_xpath(".//span[@class='price-det']").text)

    # 平方单价
    # print(li.find_element_by_xpath(".//span[@class='unit-price']").text)


print(len(ret1))

