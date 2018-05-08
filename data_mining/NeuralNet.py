import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import *
from sklearn.metrics import *
from sklearn.neural_network import MLPClassifier

DS_default_or_not_numeric = pd.read_csv("csv/DS_default_or_not_numeric.csv", delimiter=";")

DS_label = [row[-1] for row in DS_default_or_not_numeric.values]
DS_sample = np.delete(DS_default_or_not_numeric.values, -1, 1)

scaler = StandardScaler()
DS_sample = scaler.fit_transform(DS_sample)

scoring = ["accuracy", "precision", "recall"]

clf = MLPClassifier(
    hidden_layer_sizes=int((len(DS_sample[0]) + 2 ) / 2 + 1),
    max_iter=500
)
DS_predict = cross_val_predict(clf, DS_sample, DS_label, cv=10)
conf_matrix = confusion_matrix(DS_label, DS_predict)
# scores = cross_validate(gnb, DS_sample, DS_label, cv=10, scoring=scoring)

print(conf_matrix)
print(classification_report(DS_label, DS_predict))

