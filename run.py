from src.core import Kushizashi

if __name__ == '__main__':
    print 'start'
    kushi = Kushizashi()
    kushi.refresh_proxy_list()
    kushi.proxy_monitor()
    print 'end'
    datas = range(0,20) # ここにPOSTしたいデータの配列を置く(まだフォーマット未定義)
    kushi.paralell_crawling('',range(0,20))

