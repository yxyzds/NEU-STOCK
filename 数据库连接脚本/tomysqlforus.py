#coding:gbk
import json
import pymysql
conn = pymysql.connect(
        host = 'localhost',#mysql��������ַ
        port = 3306,#�˿ں�
        user = 'root',#�û���
        passwd = '19980729',#����
        db = 'users',#���ݿ�����
        charset = 'utf8',#���ӱ��룬������Ҫ��д
    )
cur = conn.cursor()#�����������α�
sql = "CREATE TABLE stocktestforus (mingcheng VARCHAR(100),zuixinjia VARCHAR(100),zhangdiefu VARCHAR(100),zhangdiee VARCHAR(100),zuigao VARCHAR(100),zuidi VARCHAR(100) ,jinkai VARCHAR(100),zuoshou VARCHAR(100),zongshizhi VARCHAR(100),shiyinglv VARCHAR(100));"
cur.execute(sql)
temp =[]
x=0 
with open('us.json','r') as file:
    str = file.read()
    data = json.loads(str)
for num in range(len(data)):
    stock = data[num]
    for key in stock:
        if stock[key]=='-':
            temp.append(stock['���'])
            break
for num in temp:
    for i in range(len(data)-10):
        if(data[i]['���'])==num:
            x=x+1
            del data[i]
for da in data:
	mingcheng=da['����']
	zuixinjia=da['���¼�(��Ԫ)']
	zhangdiefu=da['�ǵ���']
	zhangdiee=da['�ǵ���']
	zuigao=da['���']
	zuidi=da['���']
	jinkai=da['���̼�']
	zuoshou=da['����']
	zongshizhi = da['����ֵ(��Ԫ)']
	shiyinglv = da['��ӯ��']
	sql_insert =("insert into stocktestforus (mingcheng,zuixinjia,zhangdiefu,zhangdiee,zuigao,zuidi,jinkai,zuoshou,zongshizhi,shiyinglv) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
	cur.execute(sql_insert,(mingcheng,zuixinjia,zhangdiefu,zhangdiee,zuigao,zuidi,jinkai,zuoshou,zongshizhi,shiyinglv))
conn.commit()
conn.close()

	
	
