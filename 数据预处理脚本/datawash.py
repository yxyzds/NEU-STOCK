#coding:gbk
import json
import re
with open('20200508.json','r') as file:
    str = file.read()
    data = json.loads(str)
temp =[]
x=0 
test = {'a':1,'b':2,'c':2}
#清除空数据
for num in range(len(data)):
    stock = data[num]
    for key in stock:
        if stock[key]=='-':
            temp.append(stock['序号'])
            break
#替换掉汉字和符号
        if key=='成交量' or  key=='成交额' or   key=='换手率' or  key=='振幅' or  key=='涨跌幅':
            if re.search('万',stock[key]):
                stock[key]=round(float(re.split('万',stock[key])[0])*10000,4)
            elif re.search('亿',stock[key]):
                stock[key]=round(float(re.split('亿',stock[key])[0])*100000000,4)
            elif re.search('%',stock[key]):
                stock[key]=round(float(re.split('%',stock[key])[0])*0.01,4)
for num in temp:
    for i in range(len(data)-1):
        if(data[i]['序号'])==num:
            x=x+1
            del data[i]
#清洗过后的数据
with open("0508_first.json","w") as file:
    file.write(json.dumps(data,indent=2,ensure_ascii=False))


#检验代码，判断空值是否删干净
#print(len(temp))
#print(x)
#for num in range(len(data)):
    #stock = data[num]
    #for key in stock:
        #if stock[key]=='-':
            #print(stock)


