#coding:gbk
import csv
import json
with open('0507_first.json','r') as jsfile:
    str = jsfile.read();
    data_old = json.loads(str)
with open('0508_first.json','r') as jsfile:
    str = jsfile.read();
    data_new = json.loads(str)
for stock in data_old:
	if '涨跌标签' not in stock:
		tags.append(stock['代码'])
dlen =len(data_old) 
for tag in tags:
	for i in range(len(data_old)-1):
		if data_old[i]['代码'] == tag:
			del data_old[i]
for stock in data_old:
	if '涨跌标签' not in stock:
		print(stock)
#with  open ('0507_second.csv','w',newline = '') as csvfile: 
  #  fieldnames =  ["序号","代码","名称" , "最新价","涨跌幅", "涨跌额","成交量",  "成交额",  "振幅",  "最高",  "最低",  "今开",  "昨收",  "量比",  "换手率",  "市盈率", "市净率",'涨跌标签'] 
    #writer  = csv.DictWriter(csvfile,  fieldnames=fieldnames)
    #writer.writeheader() 
    #for stock in data_old:
    #    writer.writerow(stock) 
