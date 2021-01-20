
#!/usr/bin/python

import pymysql
# 设置字体，不然无法显示中文
from pylab import *


# x,y轴数据
x_arr = []  # 景区名称
y_arr = []  # 销量

mpl.rcParams['font.sans-serif'] = ['SimHei']

conn = pymysql.connect(host='192.168.2.73', port=3306,
                       user="root", passwd="123456", database='test_hyx')

cur = conn.cursor()  # 获取游标

# 另一种插入数据的方式，通过字符串传入值
sql = "select * from getCity"

# get field
try:
    # 执行SQL语句
    cur.execute(sql)
    # 获取所有记录列表
    results = cur.fetchall()

    for row in results:
        cityname = row[0]
        placename = row[1]
        address = row[2]
        count = row[3]
        point = row[4]
        price = row[5]

        # 打印结果
        print("cityname=%s,placename=%s" % (cityname,placename))

        x_arr.append(placename)
        y_arr.append(count)

except:
    print("Error: unable to fetch data")

# free
cur.close()
conn.commit()
conn.close()


"""
去哪儿月销量排行榜
"""
plt.bar(x_arr, y_arr, color='rgb')  # 指定color，不然所有的柱体都会是一个颜色
plt.gcf().autofmt_xdate()  # 旋转x轴，避免重叠
plt.xlabel(u'景点名称')  # x轴描述信息
plt.ylabel(u'月销量')  # y轴描述信息
plt.title(u'拉钩景点月销量统计表')  # 指定图表描述信息
plt.ylim(0, 100)  # 指定Y轴的高度
plt.savefig('showCity')  # 保存为图片
plt.show()
