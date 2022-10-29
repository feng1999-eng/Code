from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
data=iris.data
target=iris.target

print(data)