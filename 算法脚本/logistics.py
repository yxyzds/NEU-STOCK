from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris() # ����Iris�Ǻ����������ݼ���scikit-learn�Ѿ�ԭ���Դ��ˡ�
X = iris.data[:, [2, 3]]
y = iris.target # ��ǩ�Ѿ�ת����0��1��2��
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0) # Ϊ�˿�ģ����û�м������ݼ��ϵı��֣�����ó����ݼ���30%�Ĳ���������

# Ϊ��׷�����ѧϰ�����Ż��㷨��������ܣ����ǽ���������
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
