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
	if '�ǵ���ǩ' not in stock:
		tags.append(stock['����'])
dlen =len(data_old) 
for tag in tags:
	for i in range(len(data_old)-1):
		if data_old[i]['����'] == tag:
			del data_old[i]
for stock in data_old:
	if '�ǵ���ǩ' not in stock:
		print(stock)
#with  open ('0507_second.csv','w',newline = '') as csvfile: 
  #  fieldnames =  ["���","����","����" , "���¼�","�ǵ���", "�ǵ���","�ɽ���",  "�ɽ���",  "���",  "���",  "���",  "��",  "����",  "����",  "������",  "��ӯ��", "�о���",'�ǵ���ǩ'] 
    #writer  = csv.DictWriter(csvfile,  fieldnames=fieldnames)
    #writer.writeheader() 
    #for stock in data_old:
    #    writer.writerow(stock) 
