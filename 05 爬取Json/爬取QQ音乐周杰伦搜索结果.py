import requests
from bs4 import  BeautifulSoup

json_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

for i in range(5):
    params ={
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '66451892927258617',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(i+1),
        'n': '10',
        'w': '周杰伦',
        'g_tk_new_20200303': '5381',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }

    res_music = requests.get(json_url,params=params)
    res_music = res_music.json()['data']['song']['list']

    for i in res_music:
        music_name = i['name']
        album = i['album']['name']
        time_song = i['interval']
        song_url = 'https://y.qq.com/n/yqq/song/'+i['mid']+'.html'
        print('音乐:%s\n专辑:%s\n时长:%s秒\n地址:%s'%(music_name,album,time_song,song_url))
        print('---------------------------')