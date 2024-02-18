import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl


heart = pd.read_csv("06.csv")
heart.head()
heart.tail()
heart.shape
heart.isnull().sum()
del heart['ca']
del heart['thal']
del heart['slope']
del heart['oldpeak']

heart.head()

heart.columns
heart.info()

from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator,BayesianEstimator
heart.columns

model = BayesianNetwork(
    [
        ("age", "trestbps"),
        ("age", "fbs"),
        ("sex", "trestbps"),
        ("exang", "trestbps"),
        ("trestbps", "heartdisease"),
        ("fbs", "heartdisease"),
        ("heartdisease", "restecg"),
        ("heartdisease", "thalach"),
        ("heartdisease", "chol"),
    ]
)

# print('\n Learning CPD using Maximum likelihood estimators')
model.fit(heart,estimator=MaximumLikelihoodEstimator)

print(model.get_cpds('age'))
print(model.get_cpds('sex'))
print(model.get_cpds('fbs'))
