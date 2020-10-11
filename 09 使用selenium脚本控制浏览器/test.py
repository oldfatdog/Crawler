# 本地Chrome浏览器设置方法
from selenium import  webdriver 
import time,requests

driver = webdriver.Chrome() 

driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
login = driver.find_element_by_id('user_login')
login.send_keys('oldfatdog')
pwd = driver.find_element_by_id('user_pass')
pwd.send_keys('hz1991')
botten = driver.find_element_by_id('wp-submit')
botten.click()
time.sleep(2)

driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn')
article_link = driver.find_element_by_partial_link_text('同九义何汝秀')
link = article_link.get_attribute('href')
time.sleep(2)

driver.get(link)
coment_box = driver.find_element_by_tag_name('textarea')
coment_box.send_keys('selenium master')
botten = driver.find_element_by_id('submit')
botten.click()
time.sleep(2)

driver.close()