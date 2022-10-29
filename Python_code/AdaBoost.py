# coding=GBK
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

df = pd.read_excel('信用卡精准营销模型.xlsx')
X = df.drop(columns='响应')
Y = df['响应']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=123)
clf = AdaBoostClassifier(random_state=123)
clf.fit(X_train, Y_train)
y_perd = clf.predict(X_test)
print(y_perd)
