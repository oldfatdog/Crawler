import requests
from bs4 import BeautifulSoup
res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
html = res.text
soup = BeautifulSoup(html,'html.parser')
comments = soup.find_all(class_='wc-comment-text')
#reply_comments = soup.find_all(class_='wc-comment wc-reply wc-blog-user wc-blog-subscriber wc_comment_level-2')
for comment in comments:
    comment= comment.find('p')
#    reply_comment=reply_comments.find('p')
    print(comment.text)