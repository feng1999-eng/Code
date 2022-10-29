# coding=GBK
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = [[1], [2], [4], [5]]
Y = [2, 4, 6, 8]
reg = LinearRegression()
reg.fit(X, Y)
y = reg.predict([[1.5], [2.5], [4.5]])
print(y)
plt.scatter(X, Y)
plt.plot(X, reg.predict(X))
plt.show()
print('一元线性回归方程为：'+'y='+str(reg.coef_[0])+'x'+'+'+str(reg.intercept_))
