#coding:gbk
import numpy as np
import csv
fr = open('0506_second3.csv')
#读取文件所有内容
arrayOLines = fr.readlines()
    #得到文件行数
numberOfLines = len(arrayOLines)
returnMat = np.zeros((numberOfLines,14))
index = 0
for line in arrayOLines:
        #s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
    line = line.strip()
        #使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
    listFromLine = line.split(',')
        #将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
    returnMat[index,:] = listFromLine[2:16]
        #根据文本中标记的喜欢的程度进行分类,1代表不喜欢,2代表魅力一般,3代表极具魅力
    index += 1
print(returnMat)
def autoNorm(dataSet):
    #获得数据的最小值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    #最大值和最小值的范围
    ranges = maxVals - minVals
    #shape(dataSet)返回dataSet的矩阵行列数
    normDataSet = np.zeros(np.shape(dataSet))
    #返回dataSet的行数
    m = dataSet.shape[0]
    #原始值减去最小值
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    #除以最大和最小值的差,得到归一化数据
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    #返回归一化数据结果,数据范围,最小值
    return normDataSet, ranges, minVals
x = autoNorm(returnMat)
np.savetxt("new.csv", x,fmt='%s')
