import requests 

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'} 

url = 'https://www.shanbay.com/api/v1/vocabtest/category/?_=1588432774826'

res = requests.get(url,headers=headers)
res = res.json()['data']

for i in res:
    print(res.index(i),i)

choice = int(input('请选择题库编号'))
test = res[choice]

url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='

test_url = url+test[0]

res = requests.get(test_url,headers=headers)
res = res.json()['data']
list_all = []
for i in res:
    list_all.append(i['content'])
    
#新增一个list，用于统计用户认识的单词

#创建一个空的列表，用于记录用户认识的单词。
words_knows = []
#创建一个空的列表，用于记录用户不认识的单词。
not_knows = []
#启动一个循环，循环的次数等于单词的数量。
for i in list_all:
    #记得加一个\n，用于换行。
    print(i+'\n')
    #让用户输入自己是否认识。
    choice = input('是否认识,是y否n')
    #如果用户认识：
    if choice == 'y':
        #就把这个单词，追加进列表words_knows。
        words_knows.append(i)
    #否则
    else:    
        #就把这个单词，追加进列表not_knows。 
        not_knows.append(i)
#打印一个统计数据：这么多单词，认识几个，认识的有哪些？
# print('认识的单词:')
# print(words_knows)
# print('---------------------')
# print('不认识的单词')
# print(not_knows)

wrong_list=[]

for i in res:
    for j in words_knows:
        if i['content'] == j:
            print(j)
            for x in i['definition_choices']:
                print(i['definition_choices'].index(x),x['definition'])
            choice = int(input('请选择您认为正确的选项'))
            if i['definition_choices'][choice]['pk'] != i['pk']:
                wrong_list.append(j)

print('您认识的单词有')
print(words_knows)
print('--------------')
print('您不认识的单词有')
print(not_knows)
print('--------------')
print('您认识的单词中,掌握不好的有')
print(wrong_list)