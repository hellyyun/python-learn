#!/usr/bin/python

import requests
import re
import json
 
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
 
def get_page(url):
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)
 
stock_list_url='http://21.push2.eastmoney.com/api/qt/clist/get?cb=jQuery11240216110963949796_1586611666127&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1586611666172'
 
def get_stock_list(stock_list_url):
    try:
        stock_list=[]
        page=get_page(stock_list_url)
        print(page)
 
        stocks2 = page.replace(");" , "")
        print("stock2:"+ stocks2)
        stocks = stocks2.replace("jQuery11240216110963949796_1586611666127(" , "")
        print("stocks:" + stocks)
        stocks = json.loads(stocks)
 
        print("okma1")
        stocks=stocks["data"]["diff"]
 
        stocks = str(stocks)
 
        print("okma")
 
        stocks = stocks.replace("[" , "")
        stocks = stocks.replace("]" , "")
        stocks = stocks.replace("{" , "")
        stocks = stocks.replace("," , "")
 
        stocks = stocks.split("}")
 
        for stock in stocks:
             print("stock:" + stock)
             stock=re.findall("f12': '(.*?)' 'f13", stock)
             print("stock:" + str(stock))
             stock_list.append(stock)
 
        return stock_list
    except Exception as e:
        print(e)
 
def get_stock_info(url,stock):
    try:
        stock_info={}
        page=get_page(url)
        name=re.findall('<div class="stock-name">(.*?)<',page,re.S)
        name=name[0]
        stock_info['stock']=name
        stock_info['num']=stock
        datas=re.findall(r'<td>(.*?)<span.*?>(.*?)</span>',page,re.S)
        for data in datas:
            key=data[0]
            val=data[1]
            stock_info[key]=val
        with open('stock.txt',"a",encoding="utf-8") as f:
            f.write(str(stock_info) + '\n')
    except Exception as e:
        print(e)
 
stock_list=get_stock_list(stock_list_url)
count=0
for stock in stock_list:
    stock = str(stock)
    stock = stock.replace("[", "")
    stock = stock.replace("]", "")
    stock = stock.replace("'", "")
    stock = stock.replace("'", "")
    stock_info_url='https://xueqiu.com/S/SZ'+str(stock)
    print("stock_info_url:"+stock_info_url)
    get_stock_info(stock_info_url,stock)
    count=count+1
    print('\r当前进度:{:.2f}%'.format(count*100/len(stock_list)),end='')