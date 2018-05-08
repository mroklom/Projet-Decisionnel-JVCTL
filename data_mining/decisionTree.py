import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import *
from sklearn.metrics import *
import graphviz


DS_default_or_not_numeric = pd.read_csv("csv/DS_default_or_not_numeric.csv", delimiter=";")

DS_label = [row[-1] for row in DS_default_or_not_numeric.values]
DS_sample = np.delete(DS_default_or_not_numeric.values, -1, 1)
DS_features_names = np.delete(list(DS_default_or_not_numeric), -1)

scoring = ["accuracy", "precision", "recall"]

clf = tree.DecisionTreeClassifier(max_depth=4)
clf.fit(DS_sample, DS_label)

DS_predict = cross_val_predict(clf, DS_sample, DS_label, cv=10)
conf_matrix = confusion_matrix(DS_label, DS_predict)
# scores = cross_validate(clf, DS_sample, DS_label, cv=10, scoring=scoring)

print(conf_matrix)
print(classification_report(DS_label, DS_predict))

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=DS_features_names,
                                class_names=["False", "True"],
                                filled=True, rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("decision_tree/decisionTree1")
