#!/usr/bin/env python3
#__*__coding: utf8__*__
import re
import time
import requests
from urllib.parse import urlencode

def get_index(keyword,pages):
    title_list = []
    nick_list = []
    view_pic_list = []
    view_sal_list = []
    loc_list = []

    total_dic = {
        'title':title_list,
        'nick':nick_list,
        'view_pic':view_pic_list,
        'view_sal':view_sal_list,
        'loc':loc_list
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'Cookie':'thw=cn; isg=BAMDcRHdW2c_5BeT25Rv5jb6kc5t0Lci8GnRNzXgdGLZ9CIWvE04CrEiakQfz--y; cna=h+yUFKAYcikCAXzNMYIDsvU5; t=70661c18a1da5de47bf858db08d6b490; cookie2=1192c63b6d06f37b8fdf850e5c362eef; v=0; _tb_token_=e3e61383a38b5; unb=806957801; uc1="cookie15=URm48syIIVrSKA%3D%3D"; sg=115; _l_g_=Ug%3D%3D; skt=653ef3768574d59e; cookie1=UoTaTqt8fdFnsOsDtOyOPwwu2EKPDNDuIXLE%2FR%2FrBX0%3D; csg=e7b20f2e; uc3=vt3=F8dByRzKEY%2F1EyA6jF4%3D&id2=W8nSbtj6V3Ys&nk2=D8rsInwNjCYarj1Z&lg2=VFC%2FuZ9ayeYq2g%3D%3D; existShop=MTU0NDQyMTAyNA%3D%3D; tracknick=lijiying1991; lgc=lijiying1991; _cc_=UIHiLt3xSw%3D%3D; dnk=lijiying1991; _nk_=lijiying1991; cookie17=W8nSbtj6V3Ys; tg=0; mt=ci=3_1; enc=3oVfEoBlsCSGMITYiBZmDRXoS2bFx1cO2QC%2BgcofKCJzNnKRBvyTUHXtHB3%2FBu1gIg0tt%2FuG8NHviTV%2F%2F0vzGQ%3D%3D; JSESSIONID=65CCE7EAD8BBD2B9CB3A4612F3957669; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; swfstore=3617',
      #  'cookie': 'enc=VEHX3abvqzAizTtesaRgCwE0ol0RcdVlGoSUIsL0U3ZRcFO45nSAm0XveshuRfv%2Bl%2FKixM7IzpJCLZ4bpovQaw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=8206117252019499985; UM_distinctid=1675a47ab34204-04d8e9ce3ccfbc-10724c6f-1fa400-1675a47ab363c6; _uab_collina=154375805251262970098158; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _m_h5_tk=37e1d37782db47ff0e1d99a21f57eb7c_1544246134979; _m_h5_tk_enc=13c21511efe434b78bae233889a5f83b; cna=QxAGEp2gbW4CAXTqAfKLmcB3; t=9082eb95f822ef6cb034a2876ce5510f; uc3=vt3=F8dByR1e6h%2B%2FLx%2FS2%2F0%3D&id2=WvKUXJlaezvq&nk2=txBMnYSX&lg2=URm48syIIVrSKA%3D%3D; tracknick=%5Cu4E91%5Cu4E4B%5Cu6740; lgc=%5Cu4E91%5Cu4E4B%5Cu6740; _cc_=W5iHLLyFfA%3D%3D; tg=0; mt=ci=1_1&np=; cookie2=1141d76a6305fcdf55958bf10bf14224; v=0; _tb_token_=5663548ee3b34; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=DDF6CF07BFE7032958CF93253AC6F9F7; uc1=cookie14=UoTYMh2PRIAoBA%3D%3D; isg=BKCgG_5E6O7SSFPpXRnLu3a2f66yAZYXNpQT0hqxIrtOFUA_wrnTAz_vqf0wvjxL',
    }
    for page in range(1,pages):
        data = {
            'q': keyword,
            'ie': 'utf8',
            's': page*44
        }

        url = 'https://s.taobao.com/search?' + urlencode(data)
        print(url)
        response = requests.get(url,headers=headers)
        time.sleep(5)

        html = response.text
        #print(html)
        title = re.compile('"raw_title":"(.*?)"', re.S).findall(html)
        nick = re.compile('"nick":"(.*?)"', re.S).findall(html)
        view_pic = re.compile('"view_price":"(.*?)"', re.S).findall(html)
        view_sal = re.compile('"view_sales":"(.*?)人付款"', re.S).findall(html)
        loc = re.compile('"item_loc":"(.*?)"', re.S).findall(html)

        if title == [] or nick == [] or view_pic == [] or view_sal == [] or loc == []:
            continue
        else:
            title_list.append(title)
            nick_list.append(nick)
            view_pic_list.append(view_pic)
            view_sal_list.append(view_sal)
            loc_list.append(loc)

    print(total_dic)
    num = min(len(title_list),len(nick_list),len(view_pic_list),len(view_sal_list),len(loc_list))
    print(num)
    keys = list(total_dic.keys())
    print(keys)
    for i in range(num):
        title = total_dic[keys[0]][i]
        nick = total_dic[keys[1]][i]
        view_pic = total_dic[keys[2]][i]
        view_sal = total_dic[keys[3]][i]
        loc = total_dic[keys[4]][i]

        print(title,nick,view_pic,view_sal,loc)


def handle_page(html):
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

if __name__ == '__main__':
    get_index('游戏机', 10)
