import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
iris = load_iris()
y = iris.target
X = iris.data
#作为数组，X是几维？
print(X.shape)
#作为数据表或特征矩阵，X是几维？
import pandas as pd
pd.DataFrame(X)
pca = PCA(n_components=2)           #实例化
pca = pca.fit(X)                    #拟合模型
X_dr = pca.transform(X)             #获取新矩阵
X_dr[y == 0, 0] #这里是布尔索引，看出来了么？
#要展示三中分类的分布，需要对三种鸢尾花分别绘图
#可以写成三行代码，也可以写成for循环
"""
plt.figure()
plt.scatter(X_dr[y==0, 0], X_dr[y==0, 1], c="red", label=iris.target_names[0])
plt.scatter(X_dr[y==1, 0], X_dr[y==1, 1], c="black", label=iris.target_names[1])
plt.scatter(X_dr[y==2, 0], X_dr[y==2, 1], c="orange", label=iris.target_names[2])
plt.legend()
plt.title('PCA of IRIS dataset')
plt.show()
"""
colors = ['red', 'black', 'orange']
plt.figure()
for i in [0, 1, 2]:
    plt.scatter(X_dr[y == i, 0]
                ,X_dr[y == i, 1]
                ,alpha=.7
                ,c=colors[i]
                ,label=iris.target_names[i]
               )
plt.legend()
plt.title('PCA of IRIS dataset')
plt.show()