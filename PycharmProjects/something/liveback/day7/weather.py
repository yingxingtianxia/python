#!/usr/bin/env python3
#__*__coding: utf8__*__
import requests
import pprint
import sys


url_get = 'http://www.weather.com.cn/data/list3/city%s.xml?level=%s'
url_query = 'http://www.weather.com.cn/data/sk/%s.html'

def get_province():
    provinces_dic = {}
    response_province = requests.get(url_get % ("",1),)
    response_province.encoding = 'utf-8'
    prov_data = response_province.text.split(",")
    for provinces in prov_data:
        province_id,province = provinces.split('|')
        provinces_dic[province] = province_id
    return provinces_dic


def get_city(provinces_dic):
    province_city_dic = {}

    for province in provinces_dic.keys():
        city_dic = {}
        province_id = provinces_dic[province]
        if int(province_id) < 5:
            province_city_dic[province] = province_id
        else:
            response_city = requests.get(url_get % (province_id,2))
            response_city.encoding = 'utf-8'
            city_data = response_city.text.split(',')
            for citys in city_data:
                city_id,city = citys.split('|')
                city_dic[city] = city_id[2:]

            province_city_dic[province] =city_dic

    return province_city_dic

def get_district(province_dic,province_city_dic):
    province_city_district_dic = {}

    for province in province_dic.keys():
        district_dic = {}
        province_id = province_dic[province]
        if int(province_id) < 5:
            city_id = province_id+'01'
            resoponse_district = requests.get(url_get % (city_id, 3))
            resoponse_district.encoding = 'utf-8'
            district_data = resoponse_district.text.split(',')
            for districts in district_data:
                district_id, district = districts.split('|')
                district_dic[district] = district_id

                province_city_district_dic[province] = district_dic

        else:
            for c_id in province_city_dic[province].values():
                city_id = province_id + c_id

                resoponse_district = requests.get(url_get % (city_id, 3))
                resoponse_district.encoding = 'utf-8'
                district_data = resoponse_district.text.split(',')
                for districts in district_data:
                    district_id, district = districts.split('|')
                    district_dic[district] = district_id

                    province_city_district_dic[province] = district_dic

    return province_city_district_dic


def query_weather(district_id):

    r_w = requests.get(url_query % district_id)
    r_w.encoding = 'utf-8'

    weather_info = r_w.json()

    return weather_info

def query_zxs(province_city_district_dic,query):
    district = list(province_city_district_dic[query].keys())
    print('可以查询的地区有：' ,district)
    query_two = input('请输入需要查询的地区：')

    if query_two not in district:
        print('输入有误')
    else:
        district_id = province_city_district_dic[query][query_two]
        d_id = '1'+ district_id + '00'
        weather_info = query_weather(d_id)

    return weather_info

def query_sf(province_city_district_dic,query):
    city = list(province_city_district_dic[query].keys())
    print('%s省可查询的城市有：' % query,city)

    query_two = input('请输入需要查询的城市：')

    if query_two not in city:
        print('输入有误')
    else:
        district_id = province_city_district_dic[query][query_two]
        d_id = '101' + district_id
        weather_info = query_weather(d_id)

    return weather_info

if __name__ == '__main__':
    p_dic = get_province()
    p_c_dic = get_city(p_dic)
    print(p_c_dic)
    p_c_d_dic = get_district(p_dic, p_c_dic)
    print(p_c_d_dic)

    prompt1 = '直辖市提供二级查询（直辖市/地区），省份提供二级查询（省份/城市）'

    zxs_list = []
    sf_list = []
    p_list = list(p_dic.keys())
    for i in range(len(p_list)):
        if i <= 3:
            zxs_list.append(p_list[i])
        else:
            sf_list.append(p_list[i])

    prompt2 = '直辖市有：'
    prompt3 = '省份有：'

    print(prompt1)
    print(prompt2,zxs_list)
    print(prompt3,sf_list)

    query = input('请输入省份或直辖市：')
    if query in zxs_list:
        info = query_zxs(p_c_d_dic,query)
        pprint.pprint(info)
    elif query in sf_list:
        info = query_sf(p_c_d_dic,query)
        pprint.pprint(info)
    else:
        print('输入有误')