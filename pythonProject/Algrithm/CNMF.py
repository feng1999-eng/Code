import numpy as np
import random


def cnmf(X, C, r, k, e):
    '''
    X是原始矩阵，维度为d*n
    C是有标签样本指示矩阵，维度为l*c（l——有标签的样本数量，c——类别数量）
    r是分解的两个非负矩阵的隐变量维度，要远小于原始矩阵的维度
    k是迭代次数
    e是理想误差

    input X,C
    output U,V
    '''
    d, n = X.shape
    l, c = C.shape

    # 计算A矩阵
    I = np.mat(np.identity(n - l))
    A = np.zeros((n, n + c - l))

    for i in range(l):
        for j in range(c):
            A[i, j] = C[i, j]

    for i2 in range(n - l):
        A[l + i2, c + i2] = I[i2, i2]
    A = np.mat(A)
    U = np.mat(np.random.rand(d, r))
    Z = np.mat(np.random.rand(n + c - l, r))

    # print(A)

    x = 1
    for x in range(k):
        print('---------------------------------------------------')
        print('开始第', x, '轮迭代')
        # error
        X_pre = U * (A * Z).T
        E = X - X_pre
        # print E
        err = 0.0
        for i in range(d):
            for j in range(n):
                err += E[i, j] * E[i, j]
        print('误差：', err)

        if err < e:
            break
        # update U
        a_u = U * Z.T * A.T * A * Z
        b_u = X * A * Z
        for i_1 in range(d):
            for j_1 in range(r):
                if a_u[i_1, j_1] != 0:
                    U[i_1, j_1] = U[i_1, j_1] * b_u[i_1, j_1] / a_u[i_1, j_1]
        # print(U)

        # update Z
        # print(Z.shape,n,r)
        a_z = A.T * A * Z * U.T * U
        b_z = A.T * X.T * U
        for i_2 in range(n + c - l):
            for j_2 in range(r):
                # print(i_2, j_2, a_z[i_2,j_2])
                if a_z[i_2, j_2] != 0:
                    Z[i_2, j_2] = Z[i_2, j_2] * b_z[i_2, j_2] / a_z[i_2, j_2]
        # print(V)
        print('第', x, '轮迭代结束')

    V = (A * Z).T
    return U, V


if __name__ == "__main__":
    X = [[5, 3, 2, 1, 2, 3],
         [4, 2, 2, 1, 1, 5],
         [1, 1, 2, 5, 2, 3],
         [1, 2, 2, 4, 3, 2],
         [2, 1, 5, 4, 1, 1],
         [1, 2, 2, 5, 3, 2],
         [2, 5, 3, 2, 2, 5],
         [2, 1, 2, 5, 1, 1], ]  # 8*6,6个样本
    X = np.mat(X)
    C = [[0, 0, 1],
         [0, 1, 0],
         [0, 1, 0],
         [1, 0, 0], ]  # 4*3，假设有4个样本有标签，总共有三类标签
    # print(X)
    C = np.mat(C)
    U, V = cnmf(X, C, 2, 1000, 0.01)
    print(U.shape, V.shape)
    print(U * V)