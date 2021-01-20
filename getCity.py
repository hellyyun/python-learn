#!/usr/bin/python

import pymysql
from pylab import *
import requests
from bs4 import BeautifulSoup
#from pymongo import MongoClient

class QuNaEr():
    def __init__(self, keyword, page=1):
        self.keyword = keyword
        self.page = page

    def qne_spider(self):
        url = 'https://piao.qunar.com/ticket/list.htm?keyword=%s&region=&from=mpl_search_suggest&page=%s' % (
            self.keyword, self.page)
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        bs_obj = BeautifulSoup(text, 'html.parser')

        arr = bs_obj.find('div', {'class': 'result_list'}).contents
        for i in arr:
            info = i.attrs
            # 景区名称
            name = info.get('data-sight-name')
            # 地址
            address = info.get('data-address')
            # 近期售票数
            count = info.get('data-sale-count')
            # 经纬度
            point = info.get('data-point')

            # 起始价格
            price = i.find('span', {'class': 'sight_item_price'})
            price = price.find_all('em')
            price = price[0].text

            # insert mysql
            conn = pymysql.connect(host='192.168.2.73', port=3306, user="root", passwd="123456",database='test_hyx')

            #print(conn)

            cur = conn.cursor()  # 获取游标

            # 创建user表
            #cur.execute('drop table if exists user')

            print(self.keyword)
            print(name)
            print(address)

            # 另一种插入数据的方式，通过字符串传入值
            # sql = "truncate tabl getCity;"
            sql = "insert into getCity values('%s','%s','%s','%s','%s','%s');" % (self.keyword,name,address,count,point,price)
            cur.execute(sql)

            cur.close()
            conn.commit()
            conn.close()


# get
if __name__ == '__main__':
    citys = ['厦门']
    for i in citys:
        for page in range(1, 5):
            qne = QuNaEr(i, page=page)
            qne.qne_spider()

