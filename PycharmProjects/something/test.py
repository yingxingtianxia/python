# encoding:utf8
import pymysql
import requests
from urllib.parse import urlencode
import re
from random import choice
from requests.exceptions import RequestException

uapools = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleW\
      ebKit/537.36 (KHTML, like Gecko) Chr\
      ome/51.0.2704.79 Safari/537.36 Edge/14.14393",
     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWeb\
      Kit/537.36 (KHTML, like Gecko) Chr\
      ome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
]

headers = {
    'cookie': 'enc=VEHX3abvqzAizTtesaRgCwE0ol0RcdVlGoSUIsL0U3ZRcFO45nSAm0XveshuRfv%2Bl%2FKixM7IzpJCLZ4bpovQaw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=8206117252019499985; UM_distinctid=1675a47ab34204-04d8e9ce3ccfbc-10724c6f-1fa400-1675a47ab363c6; _uab_collina=154375805251262970098158; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _m_h5_tk=37e1d37782db47ff0e1d99a21f57eb7c_1544246134979; _m_h5_tk_enc=13c21511efe434b78bae233889a5f83b; cna=QxAGEp2gbW4CAXTqAfKLmcB3; t=9082eb95f822ef6cb034a2876ce5510f; uc3=vt3=F8dByR1e6h%2B%2FLx%2FS2%2F0%3D&id2=WvKUXJlaezvq&nk2=txBMnYSX&lg2=URm48syIIVrSKA%3D%3D; tracknick=%5Cu4E91%5Cu4E4B%5Cu6740; lgc=%5Cu4E91%5Cu4E4B%5Cu6740; _cc_=W5iHLLyFfA%3D%3D; tg=0; mt=ci=1_1&np=; cookie2=1141d76a6305fcdf55958bf10bf14224; v=0; _tb_token_=5663548ee3b34; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=DDF6CF07BFE7032958CF93253AC6F9F7; uc1=cookie14=UoTYMh2PRIAoBA%3D%3D; isg=BKCgG_5E6O7SSFPpXRnLu3a2f66yAZYXNpQT0hqxIrtOFUA_wrnTAz_vqf0wvjxL',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': str(choice(uapools))
}

def Get_ip():
    con = pymysql.connect(host='127.0.0.1',user='root',passwd='root123',db='ipdata',charset='utf8')
    cur = con.cursor()
    cur.execute('select ip_proxy from iptb')
    proxies = str(choice(cur.fetchall())[0])
    con.commit()
    con.close()
    return proxies

def get_index(keyword, page):
    data = {
        'q': keyword,
        'ie': 'utf8',
        's': page
    }
    url = 'https://s.taobao.com/search?' + urlencode(data)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页失败')
        return None

def parse_indexpage(html):
    title = re.compile('"raw_title":"(.*?)"', re.S).findall(html)
    nick = re.compile('"nick":"(.*?)"', re.S).findall(html)
    view_pic = re.compile('"view_price":"(.*?)"', re.S).findall(html)
    view_sal = re.compile('"view_sales":"(.*?)人付款"', re.S).findall(html)
    loc = re.compile('"item_loc":"(.*?)"', re.S).findall(html)
    results = {
        'title': title,
        'nick': nick,
        'view_pic': view_pic,
        'view_sal': view_sal,
        'loc': loc
    }
    return results

def Create_databases():
    con = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='taobao',charset='utf8')
    cur = con.cursor()
    sql_create = "create table steam(id int(11) auto_increment primary key, name varchar(100), shop varchar(50), price varchar(20), sales varchar(20), deal varchar(20))ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8"
    cur.execute("drop table if exists steam")
    cur.execute(sql_create)
    con.close()

#问题出在写入数据库中
def Insert_mysql(results):
    con = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='taobao',charset='utf8')
    cur = con.cursor()
    keys = list(results.keys())
    for i in range(len(results[keys[0]])):
        name = results[keys[0]][i]
        shop = results[keys[1]][i]
        price = results[keys[2]][i]
        sales = results[keys[3]][i]
        deal = results[keys[4]][i]
        cur.execute("insert into steam(name, shop, price, sales, deal) values('"+str(name)+"','"+str(shop)+"','"+str(price)+"','"+str(sales)+"','"+str(deal)+"')")
        con.close()

def main():
    Create_databases()
    count = 0
    for i in range(0, 100):
        #print('当前使用的IP代理：' + str(Get_ip()))
        print('---------当前爬取第' + str(i) + '页商品数据---------')
        html = get_index('steam游戏', str(i * 44))
        results = parse_indexpage(html)
        print(results)
        # Create_databases()
        if results['title'] == []:
            continue
        else:
            Insert_mysql(results)
        count += i
    print(count)
if __name__ == '__main__':
    main()
