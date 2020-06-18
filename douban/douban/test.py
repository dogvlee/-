# import requests
# import time
# import random
# import json
# url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=20&genres=%E7%88%B1%E6%83%85'
# proxy = {
#     'http': '112.245.21.200:38257'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
# }
# p = requests.get('https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&genres=%E5%8E%86%E5%8F%B2', headers=headers, proxies=proxy)
# print(p.text)

# data2="{'code': '10001', 'msg': '获取成功', 'data': {'count': 5, 'proxy_list': [{'ip': '124.113.192.40', 'port': 21653, 'timeout': 180, 'cometime': 180}, {'ip': '171.11.102.210', 'port': 25576, 'timeout': 324, 'cometime': 36}, {'ip': '106.46.201.168', 'port': 59669, 'timeout': 184, 'cometime': 176}, {'ip': '113.122.43.211', 'port': 22578, 'timeout': 306, 'cometime': 54}, {'ip': '123.8.249.112', 'port': 58595, 'timeout': 264, 'cometime': 96}]}}"
# data3=eval(data2)
# print(data3['data']['proxy_list'][:]['ip'])

musices=['%E9%9F%B3%E4%B9%90','%E6%AD%8C%E8%88%9E']
supenses = ['%E6%82%AC%E7%96%91', '%E6%83%8A%E6%82%9A', '%E6%81%90%E6%80%96']
for music in musices:
    for x in range(0, 40, 20):
        page = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=' + str(
            x) + '&genres='+music
        print(page)