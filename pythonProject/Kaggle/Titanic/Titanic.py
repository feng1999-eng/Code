import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("../Titanic/titanic/train.csv")
train_target = train_data['Survived']
test_data = pd.read_csv("./titanic/test.csv")
mean_train = train_data['Age'].mean()
mean_test = test_data['Age'].mean()
train_data['Age'] = train_data['Age'].fillna(mean_train)
test_data['Age'] = test_data['Age'].fillna(mean_test)
print(test_data['Age'])
X = pd.get_dummies(train_data[['Pclass', 'Sex', 'SibSp', 'Parch','Age']])
X_test = pd.get_dummies(test_data[['Pclass', 'Sex', 'SibSp', 'Parch','Age']])
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, train_target)
predictions = model.predict(X_test)
output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('./titanic/my_submission.csv', index=False)
print("Done!")
