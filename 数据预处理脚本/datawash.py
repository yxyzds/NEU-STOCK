#coding:gbk
import json
import re
with open('20200508.json','r') as file:
    str = file.read()
    data = json.loads(str)
temp =[]
x=0 
test = {'a':1,'b':2,'c':2}
#���������
for num in range(len(data)):
    stock = data[num]
    for key in stock:
        if stock[key]=='-':
            temp.append(stock['���'])
            break
#�滻�����ֺͷ���
        if key=='�ɽ���' or  key=='�ɽ���' or   key=='������' or  key=='���' or  key=='�ǵ���':
            if re.search('��',stock[key]):
                stock[key]=round(float(re.split('��',stock[key])[0])*10000,4)
            elif re.search('��',stock[key]):
                stock[key]=round(float(re.split('��',stock[key])[0])*100000000,4)
            elif re.search('%',stock[key]):
                stock[key]=round(float(re.split('%',stock[key])[0])*0.01,4)
for num in temp:
    for i in range(len(data)-1):
        if(data[i]['���'])==num:
            x=x+1
            del data[i]
#��ϴ���������
with open("0508_first.json","w") as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))


#������룬�жϿ�ֵ�Ƿ�ɾ�ɾ�
#print(len(temp))
#print(x)
#for num in range(len(data)):
    #stock = data[num]
    #for key in stock:
        #if stock[key]=='-':
            #print(stock)


