import requests
from bs4 import BeautifulSoup

# 创建会话。
session = requests.session()
# 添加请求头，避免被反爬虫。
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

def login_in():
    # 登录的网址。
    login_url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    # 登录的参数。
    data = {'log': input('请输入你的账号:'),
            'pwd': input('请输入你的密码:'),
            'wp-submit': '登录',
            'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
            'testcookie': '1'}

    # 在会话下，用post发起登录请求。
    session.post(login_url, headers=headers, data=data)


def get_hotid():
    hot_url = 'https://www.xslou.com/top/allvisit_1/'

    res = requests.get(hot_url,headers=headers)
    res.encoding = 'gbk'
    res = BeautifulSoup(res.text,'html.parser')

    def get_id(url):
        id_list = list(filter(str.isdigit,url))
        book_id = ''.join(id_list)
        return book_id

    title_list = res.find_all(class_='up2')
    fition_dict = {}
    for i in title_list:
        title = i.text
        url = i.find('a')['href']
        id = get_id(url)
        fition_dict[title]=[id]
    return fition_dict

def recomend(fition_dict):
    for x,y in fition_dict:
        i = i + 1
        print(i,x)

    
def mian():
    login_in()
    recomend(get_hotid())
    book_id = input('输入推荐书籍的编号')
    recomend_url = 'https://www.xslou.com/modules/article/uservote.php?id='+str(book_id)
    session.get(recomend_url, headers=headers, cookies=session.cookies)