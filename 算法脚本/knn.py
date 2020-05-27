import csv
from sklearn import neighbors
from numpy import genfromtxt
from sklearn.model_selection import train_test_split#分割数据集
knn = neighbors.KNeighborsClassifier(n_neighbors=30)
a = open('try1.csv', 'r+')
reader = csv.reader(a)#按行读取内容
headers = next(reader)#打印出为title那行
print(headers)
dataPath = r"try1.csv"
featureList = genfromtxt(dataPath, skip_header=0,delimiter=',',usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13))
labelList = genfromtxt(dataPath, skip_header=0,delimiter=',',usecols=(14))#得到标签
x= featureList[:]
y = labelList[:]
X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25)
print(X_train.shape)
print(X_test.shape)
y_predict = knn.predict(X_test) 
#调用该对象的测试方法，主要接收一个参数：测试数据集
probility=knn.predict_proba(X_test)  
#计算各测试样本基于概率的预测
score=knn.score(X_test,y_test,sample_weight=None)
#调用该对象的打分方法，计算出准确率
print('y_predict = ')  
print(y_predict)  
    #输出测试的结果
print('y_test = ')
print(y_test)    
    #输出原始测试数据集的正确标签，以方便对比
print ('Accuracy:',score ) 
    #输出准确率计算结果
print ('probility:',probility)
