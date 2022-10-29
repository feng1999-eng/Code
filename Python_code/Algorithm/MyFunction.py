import numpy as np
from sklearn.decomposition import NMF


class Graph(object):

    def __init__(self):
        self._count = int(input('输入图的顶点的个数:'))
        self._adjlist = [[None for i in range(self._count)] for i in range(self._count)]
        # 存储顶点
        self._peak_list = []
        for i in range(self._count):
            self._peak = input('输入顶点:')
            # 将顶点添加到数组中
            self._peak_list.append(self._peak)

    # 顶点之间的关系
    def ad_relationship(self):
        print('输入顶点之间的关系')
        for i in range(self._count):
            # 顶点自身无连通，赋值为0
            self._adjlist[i][i] = 0
            for j in range(self._count):
                while self._adjlist[i][j] == None:
                    # 输入各个顶点之间的关系
                    msg = input('输入顶点%s--%s之间的关系(0表示无连通，1表示有连通)' % (self._peak_list[i], self._peak_list[j]))
                    if msg == '0' or msg == '1':
                        # 将输入的只填入邻接矩阵中
                        self._adjlist[i][j] = int(msg)
                        self._adjlist[j][i] = self._adjlist[i][j]
                    else:
                        print('输入有误....')
        # 输出
        return self._adjlist


def compute_s(b, A, d):  # b为β参数，A为邻接矩阵，d为矩阵维度
    Matrix_I = np.identity(d)
    Matrix_a = np.matrix(Matrix_I - b * A)
    Matrix_b = np.matrix(b * A)
    Matrix_S = np.linalg.inv(Matrix_a) * Matrix_b
    return Matrix_S


def My_NMF(s, k):
    model = NMF(n_components=k)
    W = model.fit_transform(s)
    H = model.components_
    return W, H


if __name__ == '__main__':
    # s = Graph()
    # A = s.ad_relationship()
    # A = np.matrix(A)
    A = [[0, 1, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 1],
         [0, 0, 0, 1, 0, 0],
         [0, 1, 1, 0, 1, 0],
         [0, 0, 0, 1, 0, 0],
         [1, 1, 0, 0, 0, 0]]
    A = np.matrix(A)
    Matrix_S = compute_s(0.2, A, 6)
    Matrix_W, Matrix_H = My_NMF(Matrix_S, 2)
    print(Matrix_W)
    print(Matrix_H)
