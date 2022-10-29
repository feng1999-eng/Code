# coding=GBK
import matplotlib.pyplot as plt
import numpy as np

A = np.arange(10)
B = np.arange(10)
plt.plot(A, B, '*')
plt.plot(A, B)
plt.show()
