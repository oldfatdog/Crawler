import requests
from bs4 import  BeautifulSoup

json_url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'

pagenum = 6
for i in range(pagenum):
    params = {
        'g_tk_new_20200303':'5381',
        'g_tk':'5381',
        'loginUin':'0',
        'hostUin':'0',
        'format':'json',
        'inCharset':'utf8',
        'outCharset':'GB2312',
        'notice':'0',
        'platform':'yqq.json',
        'needNewCode':'0',
        'cid':'205360772',
        'reqtype':'2',
        'biztype':'1',
        'topid':'102065756',
        'cmd':'6',
        'needmusiccrit':'0',
        'pagenum':str(pagenum+1),
        'pagesize':'15',
        'lasthotcommentid':'song_102065756_34536033_1471101184',
        'domain':'qq.com',
        'ct':'24',
        'cv':'10101010'
        }

    res_music = requests.get(json_url,params=params)
    res_music = res_music.json()['comment']['commentlist']
    
    for i in res_music:
        userid = i['nick']
        comment = i['rootcommentcontent']
        print('用户:%s\n评论:%s'%(userid,comment))
        print('---------------------')
        

    