import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import *
from sklearn.metrics import *

DS_default_or_not_numeric = pd.read_csv("csv/DS_default_or_not_numeric.csv", delimiter=";")

DS_label = [row[-1] for row in DS_default_or_not_numeric.values]
DS_sample = np.delete(DS_default_or_not_numeric.values, -1, 1)

scoring = ["accuracy", "precision", "recall"]

gnb = GaussianNB()
DS_predict = cross_val_predict(gnb, DS_sample, DS_label, cv=10)
conf_matrix = confusion_matrix(DS_label, DS_predict)
# scores = cross_validate(gnb, DS_sample, DS_label, cv=10, scoring=scoring)

print(conf_matrix)
print(classification_report(DS_label, DS_predict))

