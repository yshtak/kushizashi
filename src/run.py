from core import Kushizashi

if __name__ == '__main__':
    print 'start'
    kushi = Kushizashi()
    kushi.refresh_proxy_list()
    kushi.proxy_monitor()
    print 'end'

