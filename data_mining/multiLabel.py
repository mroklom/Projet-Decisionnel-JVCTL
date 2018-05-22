import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import *
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import *


DS_treePart_numeric = pd.read_csv("csv/DS_treePart_numeric.csv", delimiter=";")

DS_label = [[row[-1] for row in DS_treePart_numeric.values]]
DS_sample = np.delete(DS_treePart_numeric.values, -1, 1)
DS_label.append([row[-1] for row in DS_sample])
DS_sample = np.delete(DS_sample, -1, 1)
DS_label.append([row[-1] for row in DS_sample])
DS_sample = np.delete(DS_sample, -1, 1)
DS_label.append([row[-1] for row in DS_sample])
DS_sample = np.delete(DS_sample, -1, 1)
DS_label = np.transpose(DS_label)


DS_features_names = np.delete(list(DS_treePart_numeric), -1)

clf = tree.DecisionTreeClassifier(max_depth=4, min_samples_leaf=5)
DS_predict = cross_val_predict(clf, DS_sample, DS_label, cv=10)

print(coverage_error(DS_label, DS_predict))
print(label_ranking_average_precision_score(DS_label, DS_predict))
print(label_ranking_loss(DS_label, DS_predict))
print()

clf = MLPClassifier(
    hidden_layer_sizes=int((len(DS_sample[0]) + 4 ) / 2 + 1),
    max_iter=500
)
DS_predict = cross_val_predict(clf, DS_sample, DS_label, cv=10)

print(coverage_error(DS_label, DS_predict))
print(label_ranking_average_precision_score(DS_label, DS_predict))
print(label_ranking_loss(DS_label, DS_predict))