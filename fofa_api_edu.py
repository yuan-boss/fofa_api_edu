import base64
import requests
import threading
import queue
from colorama import init, Fore, Back, Style



def banner():
    # Initializes Colorama
    init(autoreset=True)
    print(Style.NORMAL + Fore.MAGENTA + f'{35*"-"}edu批量资产收集工具{34*"-"}')
    print(Style.NORMAL + Fore.MAGENTA + f'{15 * " "}version:0.1 | made by yuanboss | date:2023/09/09{15 * " "}')
    print(Style.NORMAL + Fore.MAGENTA + f'{88*"*"}')
    print(Style.NORMAL + Fore.MAGENTA + f'{40*"-"}yuanboss{40*"-"}')
    print(Style.NORMAL + Fore.MAGENTA + """ 
                                                   .o8                                   
                                                  "888                                   
    oooo    ooo oooo  oooo   .oooo.   ooo. .oo.    888oooo.   .ooooo.   .oooo.o  .oooo.o 
     `88.  .8'  `888  `888  `P  )88b  `888P"Y88b   d88' `88b d88' `88b d88(  "8 d88(  "8 
      `88..8'    888   888   .oP"888   888   888   888   888 888   888 `"Y88b.  `"Y88b.  
       `888'     888   888  d8(  888   888   888   888   888 888   888 o.  )88b o.  )88b 
        .8'      `V88V"V8P' `Y888""8o o888o o888o  `Y8bod8P' `Y8bod8P' 8""888P' 8""888P' 
    .o..P'                                                                               
    `Y8P'                                                                                                                                                                    
        """)
    print(Style.NORMAL + Fore.MAGENTA + f'{88*"*"}')
    print(Style.NORMAL + Fore.MAGENTA + f'{40*"-"}yuanboss{40*"-"}')

# 提示
def tip():
    print(Style.NORMAL + Fore.YELLOW + """
    该工具是基于fofa空间探测引擎，专门为搜索EDU资产定制的，内置中国大多数的高校名单\n
    你只需要根据fofa的语法，就可以自动搜索出符合条件的高校的IP地址\n
    使用帮助：
    请输入邮箱：xxxxxx@xxxx
    请输入apikey：xxxxx
    请输入搜索条件：country="CN" && title=="Error 404--Not Found"
    """)

# 获取fofa资产
def get_fofa_data(email, apikey, input, page=1, size=10):
    while not q.empty():
        try:
            eduName = q.get()
            search = f'"{eduName.strip()}" && {input}'
            qbase64 = base64.b64encode(search.encode('utf-8')).decode('utf-8')
            url = f'https://fofa.info/api/v1/search/all?email={email}&key={apikey}&qbase64={qbase64}&page={page}&size={size}'
            res = requests.get(url).json()
            print(url)
            print(res)
            if res['size'] != 0:
                print(f'{eduName.strip()}中存在相关资产，接下来进行查询数据：')
                for ip in res['results']:
                    print(ip[0])
            else:
                print(eduName.strip() + '没有相关资产')
        except Exception as e:
            print(e)
            pass

# 创建edu资产名称队列
def createQueue():
    q = queue.Queue()
    for eduName in open('eduName.txt',encoding='gb2312'):
        q.put(eduName)
    return q

if __name__ == '__main__':

    # # 搜索条件
    # input = 'country="CN" && title=="Error 404--Not Found"'
    # 页数
    page = 1
    # 一页多少条数据
    size = 10
    banner()
    tip()
    # fofa邮箱
    email = input('请输入邮箱：')
    # fofa apikey
    apikey = input('请输入apikey：')
    # input
    input = input('请输入搜索条件：')
    # 线程数
    threads = 2
    # 创建edu资产名称队列
    q = createQueue()
    for thread in range(0, threads):
        t = threading.Thread(target=get_fofa_data, args=(email, apikey, input, page, size))
        t.start()
