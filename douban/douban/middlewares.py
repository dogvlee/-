import random
import requests
from douban.models import ProxyModel
from twisted.internet.defer import DeferredLock
class UserAgentDownloadMiddleware(object):
    # user-agent随机请求头中间件
    USERAGENTS = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36',
        # 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
        # 'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        # 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
    ]

    def process_request(self, request, spider):
        user_agent = random.choice(self.USERAGENTS)
        request.headers['User-agent'] = user_agent





class IPProxy(object):
    PROXY_URL = ""

    def __init__(self):

        self.lock = DeferredLock()
        self.current_proxy = None

    def process_request(self, request, spider):
        if 'proxy' not in request.meta or self.current_proxy.is_expiring:
            self.update_proxy()
        request.meta['proxy'] = self.current_proxy.proxy

    def process_response(self, request, response, spider):
        contents = eval(response.text).get("data")

        if  contents==None:
            if not self.current_proxy.is_block:
                self.current_proxy.is_block = True
                print('%s代理失效' % self.current_proxy.proxy)
            self.update_proxy()

            return request
        return response

    def update_proxy(self):
        self.lock.acquire()
        if self.current_proxy is None or self.current_proxy.is_expiring or self.current_proxy.is_block:
            response_json = requests.get(self.PROXY_URL).json()
            try:
                print(response_json)

                self.current_proxy = ProxyModel(response_json['data'][0])

            except:
                print('出错了！')
                print(response_json)
        self.lock.release()


