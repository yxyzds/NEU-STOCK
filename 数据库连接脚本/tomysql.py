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
            temp.append(stock['���'])
            break
for num in temp:
    for i in range(len(data)-1):
        if(data[i]['���'])==num:
            x=x+1
            del data[i]
for da in data:
	daima=da['����']
	mingcheng=da['����']
	zuixinjia=da['���¼�']
	zhangdiefu=da['�ǵ���']
	zhangdiee=da['�ǵ���']
	chengjiaoliang=da['�ɽ���']
	chengjiaoe=da['�ɽ���']
	zhenfu=da['���']
	zuigao=da['���']
	zuidi=da['���']
	jinkai=da['��']
	zuoshou=da['����']
	liangbi=da['����']
	shiyinglv=da['��ӯ��']
	shijinglv=da['�о���']
	sql_insert =("insert into stocktest2 (daima,mingcheng,zuixinjia,zhangdiefu,zhangdiee,chengjiaoliang,chengjiaoe,zhenfu,zuigao,zuidi,jinkai,zuoshou,liangbi,shiyinglv,shijinglv) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
	cur.execute(sql_insert,(daima,mingcheng,zuixinjia,zhangdiefu,zhangdiee,chengjiaoliang,chengjiaoe,zhenfu,zuigao,zuidi,jinkai,zuoshou,liangbi,shiyinglv,shijinglv))
conn.commit()
conn.close()

	
	
