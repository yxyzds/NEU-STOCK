#! /usr/bin/python
# -*- encoding:utf8 -*-

import numpy as np


def rand(a, b):
    return (b - a) * np.random.random() + a

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class BP:
    def __init__(self, layer, iter, max_error):
        self.input_n = layer[0]  # �����Ľڵ���� d
        self.hidden_n = layer[1]  # ���ز�Ľڵ���� q
        self.output_n = layer[2]  # �����Ľڵ���� l
        self.gj = []
        self.eh = []
        self.input_weights = []   # ����������ز��Ȩֵ����
        self.output_weights = []  # ���ز���������Ȩֵ����
        self.iter = iter          # ����������
        self.max_error = max_error  # ֹͣ����Χ

        # for i in range(self.input_n + 1):
        #     tmp = []
        #     for j in range(self.hidden_n):
        #         tmp.append(rand(-0.2, 0.2))
        #     self.input_weights.append(tmp)
        #
        # for i in range(self.hidden_n + 1):
        #     tmp = []
        #     for j in range(self.output_n):
        #         tmp.append(rand(-0.2, 0.2))
        #     self.output_weights.append(tmp)
        # self.input_weights = np.array(self.input_weights)
        # self.output_weights = np.array(self.output_weights)

        # ��ʼ��һ��(d+1) * q�ľ��󣬶�ӵ�1�ǽ����ز�ķ�ֵ���뵽����������
        self.input_weights = np.random.random((self.input_n + 1, self.hidden_n))
        # ��ʼ��һ��(q+1) * l�ľ��󣬶�ӵ�1�ǽ������ķ�ֵ���뵽�����м򻯼���
        self.output_weights = np.random.random((self.hidden_n + 1, self.output_n))

        self.gj = np.zeros(layer[2])
        self.eh = np.zeros(layer[1])

    #  ���򴫲��뷴�򴫲�
    def forword_backword(self, xj, y, learning_rate=0.1):
        xj = np.array(xj)
        y = np.array(y)
        input = np.ones((1, xj.shape[0] + 1))
        input[:, :-1] = xj
        x = input
        # ah = np.dot(x, self.input_weights)
        ah = x.dot(self.input_weights)
        bh = sigmoid(ah)

        input = np.ones((1, self.hidden_n + 1))
        input[:, :-1] = bh
        bh = input

        bj = np.dot(bh, self.output_weights)
        yj = sigmoid(bj)

        error = yj - y
        self.gj = error * sigmoid_derivative(yj)

        # wg = np.dot(self.output_weights, self.gj)

        wg = np.dot(self.gj, self.output_weights.T)
        wg1 = 0.0
        for i in range(len(wg[0]) - 1):
            wg1 += wg[0][i]
        self.eh = bh * (1 - bh) * wg1
        self.eh = self.eh[:, :-1]

        #  ���������Ȩֵw����ΪȨֵ��������һ�б�ʾ���Ƿ�ֵ����ѭ��ֻ�������ڶ���
        for i in range(self.output_weights.shape[0] - 1):
            for j in range(self.output_weights.shape[1]):
                self.output_weights[i][j] -= learning_rate * self.gj[0][j] * bh[0][i]

        #  ��������㷧ֵb��Ȩֵ��������һ�б�ʾ���Ƿ�ֵ
        for j in range(self.output_weights.shape[1]):
            self.output_weights[-1][j] -= learning_rate * self.gj[0][j]

        #  ���������Ȩֵw
        for i in range(self.input_weights.shape[0] - 1):
            for j in range(self.input_weights.shape[1]):
                self.input_weights[i][j] -= learning_rate * self.eh[0][j] * xj[i]

        # ��������㷧ֵb
        for j in range(self.input_weights.shape[1]):
            self.input_weights[-1][j] -= learning_rate * self.eh[0][j]
        return error

    def fit(self, X, y):

        for i in range(self.iter):
            error = 0.0
            for j in range(len(X)):
                error += self.forword_backword(X[j], y[j])
            error = error.sum()
            if abs(error) <= self.max_error:
                break

    def predict(self, x_test):
        x_test = np.array(x_test)
        tmp = np.ones((x_test.shape[0], self.input_n + 1))
        tmp[:, :-1] = x_test
        x_test = tmp
        an = np.dot(x_test, self.input_weights)
        bh = sigmoid(an)
        #  ��ӵ�1�����뷧ֵ���
        tmp = np.ones((bh.shape[0], bh.shape[1] + 1))
        tmp[:, : -1] = bh
        bh = tmp
        bj = np.dot(bh, self.output_weights)
        yj = sigmoid(bj)
        print yj
        return yj

if __name__ == '__main__':
    #  ָ������������㣬���ز㣬������Ԫ�ظ���
    layer = [2, 4, 1]
    X = [
            [1, 1],
            [2, 2],
            [1, 2],
            [1, -1],
            [2, 0],
            [2, -1]
        ]
    y = [[0], [0], [0], [1], [1], [1]]
    # x_test = [[2, 3],
    #           [2, 2]]
    #  �������ĵ����������Լ�������ֵ
    bp = BP(layer, 10000, 0.0001)
    bp.fit(X, y)
    bp.predict(X)
