# coding:utf-8
import urllib
import urllib2
import datetime
import locale
import os
import re

class Kushizashi(object):
    # Cybersyndromeさんにお世話になります
    __target = 'http://www.cybersyndrome.net/pld5.html'
    name = 'test'
    proxy_list = []
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    # コンストラクタ
    def __init__(self):
        self.name = "KushizashiClass"
        proxy_list = []
    # プロキシリストを監視する
    def proxy_monitor(self):
        print self.OKGREEN + "------------------PROXY_LIST------------------" + self.ENDC
        for ip in self.proxy_list:
            print self.OKBLUE + ip + self.ENDC
        print (self.OKGREEN + "- %s ------------------" + self.ENDC ) % datetime.datetime.today()

    # プロキシリストの更新
    def refresh_proxy_list(self):
        print "REFRESH_PROXY_LIST:::\n"
        print "clawler from %s" % self.__target
        res = urllib2.urlopen(self.__target)
        html = res.read()
        # 先頭20個のプロキシ取得
        proxies = re.findall("[0-9]+\.(.*?:[0-9]+)",html)[0:20]
        self.proxy_list = proxies
        save_path = os.path.dirname(__file__) + "/../db"
        print save_path
        f = open( save_path+"/proxies" ,'w')
        # DBの更新
        f.write("[proxy_servers]\n")
        for ip in proxies:
            f.write(ip+"\n")
        f.close()
        return True
