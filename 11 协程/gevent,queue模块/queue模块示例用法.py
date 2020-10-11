# --------------------------------
# 导入gevent,queue模块，导入计时模块time，请求网页模块requests
from gevent import monkey
monkey.patch_all()
import gevent, time, requests
from gevent.queue import Queue


# --------------------------------
# queue的几个方法
# .put_nowait()     往队列里存储数据
# .get_nowait()     从队列里提取数据
# .empty()      判断队列是否为空
# .qsize()      判断队列剩余数量
# .empty()      判断队列是否为满

# --------------------------------
# 开始计时，获得程序运行的启动时间
start_time = time.time()


# --------------------------------
# 写入网址列表（这里写死了）
url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']


# --------------------------------
# 使用queue模块，创建队列对象，并赋值给work
# 用Queue()能创建queue对象，相当于创建了一个不限任何存储数量的空队列。如果我们往Queue()中传入参数，比如Queue(10)，则表示这个队列只能存储10个任务。
work = Queue()


# --------------------------------
# 把网址都放入work的列表中
for url in url_list:
    work.put_nowait(url)


# --------------------------------
# 从work列表中取出网址,并让爬虫去爬
def crawler():
    while not work.empty():
    # 当列表不为空，就从列表中取网址出来爬
        url = work.get_nowait()
        # 取出一个网址
        r = requests.get(url)
        # 请求网址
        print(url,work.qsize(),r.status_code)
        # 输出爬取结果


# --------------------------------
# 创建新的任务列表
tasks_list = []


# --------------------------------
# 创建两个爬虫任务
for i in range(2):
    task = gevent.spawn(crawler)
    # 创建爬虫任务
    tasks_list.append(task)
    # 往任务列表中添加任务


# --------------------------------
# 执行task_list列表中的所有任务
gevent.joinall(tasks_list)


# --------------------------------
# 统计运行时间
end_time = time.time()
print(end_time - start_time)


