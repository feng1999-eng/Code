# coding=GBK
import numpy as np
import matplotlib.pyplot as plt

train = np.loadtxt('click.csv', delimiter=',', skiprows=1)
train_x = train[:, 0]
train_y = train[:, 1]
mu = train_x.mean()
sigma = train_x.std()


def standardize(x):
    return (x - mu) / sigma

def to_Matrix(x):
    return np.vstack([np.ones(x.shape[0]),x,x**2]).T

train_z = standardize(train_x)
theta = np.random.rand(3)
X=to_Matrix(train_z)

def f(x):
    return np.dot(x,theta)




def E(x, y):
    return 0.5 * np.sum((y - f(x)) ** 2)


ETA = 1e-3
diff = 1
count = 0
error = E(X, train_y)
while diff > 1e-2:
    theta=theta-ETA*np.dot(f(X)-train_y,X)
    current_error = E(X, train_y)
    diff = error - current_error
    error = current_error
    count += 1
l = np.linspace(-3, 3, 100)
plt.plot(train_z, train_y, 'o')
print(f(standardize(100)))
plt.plot(l, f(to_Matrix(l)))
print(f(to_Matrix(l)))
plt.show()
