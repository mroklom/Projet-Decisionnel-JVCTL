import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import *
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import *

DS_treePart_numeric_label = pd.read_csv("csv/DS_treePartWithDisease_numeric_label.csv", delimiter=";")
DS_label = np.array(DS_treePart_numeric_label.values)


DS_treePart_numeric_multiclass_predict = pd.read_csv("csv/DS_treePartWithDisease_numeric_multiclass_predict.csv", delimiter=";")
DS_predict = np.array(DS_treePart_numeric_multiclass_predict.values)

print(coverage_error(DS_label, DS_predict))
print(label_ranking_average_precision_score(DS_label, DS_predict))
print(label_ranking_loss(DS_label, DS_predict))
print()


DS_treePart_numeric_solo_predict = pd.read_csv("csv/DS_treePartWithDisease_numeric_solo_predict.csv", delimiter=";")
DS_predict = np.array(DS_treePart_numeric_solo_predict.values)

print(coverage_error(DS_label, DS_predict))
print(label_ranking_average_precision_score(DS_label, DS_predict))
print(label_ranking_loss(DS_label, DS_predict))
print()

DS_treePart_numeric_loop_predict = pd.read_csv("csv/DS_treePartWithDisease_numeric_loop_predict.csv", delimiter=";")
DS_predict = np.array(DS_treePart_numeric_loop_predict.values)

print(coverage_error(DS_label, DS_predict))
print(label_ranking_average_precision_score(DS_label, DS_predict))
print(label_ranking_loss(DS_label, DS_predict))
print()
