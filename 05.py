'''Write a program to implement K-Nearest Neighbour algorithm to classify
the iris data set. Print both correct and wrong predictions.'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()
#iris.data[:5]

print("\n iris features",iris.target_names)

print("\n iris data \n",iris.data[:5])

X_train, X_test, y_train, y_test = train_test_split(iris["data"], iris["target"],random_state=10)

kn=KNeighborsClassifier()

kn.fit(X_train,y_train)

prediction=kn.predict(X_test)
prediction

print("\n test score [accuracy]:{:.2f}\n".format(kn.score(X_test,y_test)))

    