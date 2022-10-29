import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
cancer=datasets.load_breast_cancer()
cancer_X=cancer.data
cancer_Y=cancer.target
X_train,X_test,Y_train,Y_test=train_test_split(cancer_X,cancer_Y,test_size=0.3)
clf_tree=DecisionTreeClassifier(max_depth=1,random_state=1)
def my_adaboost_clf(Y_train, X_train, Y_test, X_test, M=20, weak_clf=DecisionTreeClassifier(max_depth=1)):
    n_train, n_test = len(X_train), len(X_test)
    # Initialize weights
    w = np.ones(n_train) / n_train
    pred_train, pred_test = [np.zeros(n_train), np.zeros(n_test)]

    for i in range(M):
        # Fit a classifier with the specific weights
        weak_clf.fit(X_train, Y_train, sample_weight=w)
        pred_train_i = weak_clf.predict(X_train)
        pred_test_i = weak_clf.predict(X_test)

        # Indicator function
        miss = [int(x) for x in (pred_train_i != Y_train)]
        print("weak_clf_%02d train acc: %.4f"
              % (i + 1, 1 - sum(miss) / n_train))

        # Error
        err_m = np.dot(w, miss)
        # Alpha
        alpha_m = 0.5 * np.log((1 - err_m) / float(err_m))
        # New weights
        miss2 = [x if x == 1 else -1 for x in miss]  # -1 * y_i * G(x_i): 1 / -1
        w = np.multiply(w, np.exp([float(x) * alpha_m for x in miss2]))
        w = w / sum(w)

        # Add to prediction
        pred_train_i = [1 if x == 1 else -1 for x in pred_train_i]
        pred_test_i = [1 if x == 1 else -1 for x in pred_test_i]
        pred_train = pred_train + np.multiply(alpha_m, pred_train_i)
        pred_test = pred_test + np.multiply(alpha_m, pred_test_i)

    pred_train = (pred_train > 0) * 1
    pred_test = (pred_test > 0) * 1

    print("My AdaBoost clf train accuracy: %.4f" % (sum(pred_train == Y_train) / n_train))
    print("My AdaBoost clf test accuracy: %.4f" % (sum(pred_test == Y_test) / n_test))
my_adaboost_clf(Y_train,X_train,Y_test,X_test)