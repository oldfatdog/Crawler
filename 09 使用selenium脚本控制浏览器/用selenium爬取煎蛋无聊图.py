# 本地Chrome浏览器设置方法
from selenium import  webdriver 
import time,requests

driver = webdriver.Chrome() 
# 开始爬取的起始页
url = 'http://jandan.net/pic'

# 选择爬取的页数
for i in range(2):

    driver.get(url)
    time.sleep(2)
    # 获取下一页
    next_page = driver.find_element_by_partial_link_text('下一页')
    url = next_page.get_attribute('href')
    # 获得无聊图地址并保存本地
    imgs_link = driver.find_elements_by_partial_link_text('[查看原图]')
    for i in imgs_link:
        img_link = i.get_attribute('href')
        pic = requests.get(img_link)
        pic = pic.content
        # 取图片链接后17个字符作为图片名
        with open(img_link[-17:],'wb') as f:
            f.write(pic)
    