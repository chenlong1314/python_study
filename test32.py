#--*-- encoding:utf-8 --*--
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import numpy as np
# mysql_cn= pymysql.connect(host='tronsi.com', port=3306,user='root', passwd='11111111', db='test1')
# df = pd.read_sql('select * from film_fen;', con=mysql_cn)
# mysql_cn.close()
# print(df)


data=pd.read_excel("student.xlsx")
print(data.head()）
