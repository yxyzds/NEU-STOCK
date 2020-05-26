#coding:gbk
import numpy as np
import csv
fr = open('0506_second3.csv')
#��ȡ�ļ���������
arrayOLines = fr.readlines()
    #�õ��ļ�����
numberOfLines = len(arrayOLines)
returnMat = np.zeros((numberOfLines,14))
index = 0
for line in arrayOLines:
        #s.strip(rm)����rm��ʱ,Ĭ��ɾ���հ׷�(����'\n','\r','\t',' ')
    line = line.strip()
        #ʹ��s.split(str="",num=string,cout(str))���ַ�������'\t'�ָ���������Ƭ��
    listFromLine = line.split(',')
        #������ǰ������ȡ����,��ŵ�returnMat��NumPy������,Ҳ������������
    returnMat[index,:] = listFromLine[2:16]
        #�����ı��б�ǵ�ϲ���ĳ̶Ƚ��з���,1����ϲ��,2��������һ��,3����������
    index += 1
print(returnMat)
def autoNorm(dataSet):
    #������ݵ���Сֵ
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    #���ֵ����Сֵ�ķ�Χ
    ranges = maxVals - minVals
    #shape(dataSet)����dataSet�ľ���������
    normDataSet = np.zeros(np.shape(dataSet))
    #����dataSet������
    m = dataSet.shape[0]
    #ԭʼֵ��ȥ��Сֵ
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    #����������Сֵ�Ĳ�,�õ���һ������
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    #���ع�һ�����ݽ��,���ݷ�Χ,��Сֵ
    return normDataSet, ranges, minVals
x = autoNorm(returnMat)
np.savetxt("new.csv", x,fmt='%s')
