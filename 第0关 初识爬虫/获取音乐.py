import requests
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
mp = res.content
with open('music.mp3','wb') as music:
    music.write(mp) 