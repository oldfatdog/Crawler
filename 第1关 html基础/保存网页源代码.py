import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
res.encoding='utf-8'
html = res.text
with open('source_code.txt','w',encoding='utf-8') as code:
    code.write(html)

import requests
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
res.encoding = 'utf-8'
html = res.text
with open('source_code.txt','w',encoding = 'utf-8')as code:
    code.write(html)
