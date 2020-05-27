from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split

a = open('try1.csv', 'r+')
reader = csv.reader(a)#按行读取内容
headers = next(reader)#打印出为title那行
print(headers)
dataPath = r"try1.csv"
featureList = genfromtxt(dataPath, skip_header=0,delimiter=',',usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13))
labelList = genfromtxt(dataPath, skip_header=0,delimiter=',',usecols=(14))#得到标签
X= featureList[:]
Y = labelList[:]
X = iris.data[:, [2, 3]]
y = iris.target # 标签已经转换成0，1，2了
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0) 


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train) 
sc.mean_ 
sc.scale_ 
X_train_std = sc.transform(X_train)

X_test_std = sc.transform(X_test)


from sklearn.linear_model import Perceptron

ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0)
ppn.fit(X_train_std, y_train)

y_pred = ppn.predict(X_test_std)
accuracy_score(y_test, y_pred)
