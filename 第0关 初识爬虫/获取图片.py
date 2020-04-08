import requests
res = requests.get('https://i.4cdn.org/wg/1579627937572.jpg')
pic = res.content
with open('picture.jpg','wb') as picture:
    picture.write(pic)