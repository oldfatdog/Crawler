import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库

def download_all_img_address(adderss):

    all_img_address = []
    res = requests.get(adderss)# 返回一个Response对象，赋值给res
    html = res.text# 把Response对象的内容以字符串的形式返回
    soup = BeautifulSoup( html,'html.parser') # 把网页解析为BeautifulSoup对象
    items = soup.find_all(class_="fileThumb")

    for item in items:
        img_address = item['href']
        all_img_address.append(img_address)
    print('已下载全部图片地址')
    return all_img_address

def download_img(all_img_address):
    print('正在下载目标图片')
    for address in all_img_address:
        res = requests.get('https:'+address)
        res = res.content
        with open(address[-17:],'wb') as img:
            img.write(res)
    print('下载完成')
    
def start_download():
    address = input('请输入网址')
    all_address = download_all_img_address(address)
    download_img(all_address)

start_download()