#coding:gbk
import csv
import json
with open('20200507.json','r') as jsfile:
    str = jsfile.read();
    data_old = json.loads(str)
with open('20200508.json','r') as jsfile:
    str = jsfile.read();
    data_new = json.loads(str)
for stock in data_old:
	if stock['代码']=='603879':
		print(stock)
for stock in data_new:
	if stock['代码']=='603879':
		print(stock)
