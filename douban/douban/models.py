#-*- coding:utf-8 -*-
from datetime import datetime, timedelta



class ProxyModel(object):
    def __init__(self, data):
        self.host = data['ip']
        self.port = data['port']
        self.timeout=data['timeout']
        self.proxy = "https://{}:{}".format(self.host, self.port)
        self.is_block = False
        print(self.proxy)

    def is_expiring(self):

        if (self.timeout)<10:
            return True
        else:
            return False

















    #     expire_str = data['expire_time']
    #     year, month, day = expire_str.split(" ")[0].split("-")
    #     hour, minute, second = expire_str.split(" ")[1].split(":")
    #     self.expire_time = datetime(int(year), int(month),int(day), int(hour), int(minute), int(second))
    #



    # @property
    # def is_expiring(self):
    #     now = datetime.now()
    #     if (self.expire_time - now)<timedelta(seconds=5):
    #         return True
    #     else:
    #         return False

    #
