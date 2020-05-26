#coding:gbk
import json
import pymysql
conn = pymysql.connect(
        host = 'localhost',#mysql服务器地址
        port = 3306,#端口号
        user = 'root',#用户名
        passwd = '19980729',#密码
        db = 'users',#数据库名称
        charset = 'utf8',#连接编码，根据需要填写
    )
cur = conn.cursor()#创建并返回游标
sql = "CREATE TABLE stocktest2 (daima  VARCHAR(100),mingcheng VARCHAR(100),zuixinjia VARCHAR(100),zhangdiefu VARCHAR(100),zhangdiee VARCHAR(100),chengjiaoliang VARCHAR(100),chengjiaoe VARCHAR(100),zhenfu VARCHAR(100),zuigao VARCHAR(100),zuidi VARCHAR(100) ,jinkai VARCHAR(100),zuoshou VARCHAR(100),liangbi VARCHAR(100),shiyinglv VARCHAR(100),shijinglv VARCHAR(100));"
cur.execute(sql)
temp =[]
x=0 
with open('20200508.json','r') as file:
    str = file.read()
    data = json.loads(str)
for num in range(len(data)):
    stock = data[num]
    for key in stock:
        if stock[key]=='-':
            temp.append(stock['序号'])
            break
for num in temp:
    for i in range(len(data)-1):
        if(data[i]['序号'])==num:
            x=x+1
            del data[i]
for da in data:
	daima=da['代码']
	mingcheng=da['名称']
	zuixinjia=da['最新价']
	zhangdiefu=da['涨跌幅']
	zhangdiee=da['涨跌额']
	chengjiaoliang=da['成交量']
	chengjiaoe=da['成交额']
	zhenfu=da['振幅']
	zuigao=da['最高']
	zuidi=da['最低']
	jinkai=da['今开']
	zuoshou=da['昨收']
	liangbi=da['量比']
	shiyinglv=da['市盈率']
	shijinglv=da['市净率']
	sql_insert =("insert into stocktest2 (daima,mingcheng,zuixinjia,zhangdiefu,zhangdiee,chengjiaoliang,chengjiaoe,zhenfu,zuigao,zuidi,jinkai,zuoshou,liangbi,shiyinglv,shijinglv) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
	cur.execute(sql_insert,(daima,mingcheng,zuixinjia,zhangdiefu,zhangdiee,chengjiaoliang,chengjiaoe,zhenfu,zuigao,zuidi,jinkai,zuoshou,liangbi,shiyinglv,shijinglv))
conn.commit()
conn.close()

	
	
