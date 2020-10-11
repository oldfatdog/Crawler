import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
res = res.text
with open('test.txt','w',encoding = 'utf-8') as t:
    t.write(res)
