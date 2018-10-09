#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests
from pyquery import PyQuery as pq
def get_data():
    titles = []
    authors = []
    descs = []
    contents = []
    datas = [titles, authors, descs, contents]
    for i in range(1, 11):
        get_url = 'http://quotes.toscrape.com/page/1'
        doc = pq(url=get_url)
        divs = doc('div.quote')
        # print(divs)
        for div in divs:
            content = pq(div)('span').text()
            author = pq(div)('small').text()
            desc = pq(div)('a').attr('href')
            title = pq(div)('div:nth-child(3) > a:nth-child(2)').text()
            # print(title, author, desc, content)
            datas[0].append(title)
            datas[1].append(author)
            datas[2].append(desc)
            datas[3].append(content)

    return datas

def put_data(datas):
    put_url = 'http://127.0.0.1:8000/blog/add'
    s = requests.Session()
    response = s.get(put_url)
    doc = pq(response.text)
    inputVal = doc('input[name="csrfmiddlewaretoken"]').val()
    # print(inputVal)
    for i in range(len(datas[0])):
        data = {
            'csrfmiddlewaretoken': inputVal,
            'title': datas[0][i],
            'author': datas[1][i],
            'desc': datas[2][i],
            'content': datas[3][i],
        }
        s.post(put_url, data=data)

    return 'Success'


if __name__ == '__main__':
    datas = get_data()
    print(len(datas[0]))
    put_data(datas)