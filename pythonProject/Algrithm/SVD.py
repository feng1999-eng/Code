import numpy as np

X = [[5, 3, 2, 1, 2, 3],
     [4, 2, 2, 1, 1, 5],
     [1, 1, 2, 5, 2, 3],
     [1, 2, 2, 4, 3, 2],
     [2, 1, 5, 4, 1, 1],
     [1, 2, 2, 5, 3, 2],
     [2, 5, 3, 2, 2, 5],
     [2, 1, 2, 5, 1, 1], ]
X = np.mat(X)
U, S, V = np.linalg.svd(X)

P = np.mat(np.zeros((8, 6)))
for i in range(6):
    for j in range(6):
        if (i == j):
            P[i, j] = S[i]
err = 0.0
E_pre = X - U * P * V
for i in range(8):
    for j in range(6):
        err += E_pre[i, j] * E_pre[i, j]
print(E_pre)
print(err)
err = (err / 48) ** 0.5
print(err)
