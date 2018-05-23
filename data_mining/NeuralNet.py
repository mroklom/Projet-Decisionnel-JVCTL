import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import *
from sklearn.metrics import *
from sklearn.neural_network import MLPClassifier
from matplotlib import pyplot as plt

DS_default_or_not_numeric = pd.read_csv("csv/DS_default_or_not_numeric.csv", delimiter=";")

DS_label = [row[-1] for row in DS_default_or_not_numeric.values]
DS_sample = np.delete(DS_default_or_not_numeric.values, -1, 1)

scaler = StandardScaler()
DS_sample = scaler.fit_transform(DS_sample)

scoring = ["recall"]

# cv = GridSearchCV(
#     estimator=MLPClassifier(max_iter=500),
#     param_grid={"hidden_layer_sizes": range(10, 201, 10)},
#     scoring=scoring,
#     refit="recall",
#     cv=3
# )
# cv.fit(DS_sample, DS_label)
# results = cv.cv_results_
# print(cv.best_params_)
#
# plt.figure(figsize=(7, 7))
# plt.title("Hidden layer size Search",
#           fontsize=12)
#
# plt.xlabel("hidden_layer_sizes")
# plt.ylabel("Recall")
# plt.grid()
#
# ax = plt.axes()
# ax.set_xlim(10, 200)
# ax.set_ylim(0.5, 1)
#
# # Get the regular numpy array from the MaskedArray
# X_axis = np.array(results['param_hidden_layer_sizes'].data, dtype=float)
#
# for scorer, color in zip(sorted(scoring), ['g', 'k']):
#     for sample, style in (('train', '--'), ('test', '-')):
#         sample_score_mean = results['mean_%s_%s' % (sample, scorer)]
#         sample_score_std = results['std_%s_%s' % (sample, scorer)]
#         ax.fill_between(X_axis, sample_score_mean - sample_score_std,
#                         sample_score_mean + sample_score_std,
#                         alpha=0.1 if sample == 'test' else 0, color=color)
#         ax.plot(X_axis, sample_score_mean, style, color=color,
#                 alpha=1 if sample == 'test' else 0.7,
#                 label="%s (%s)" % (scorer, sample))
#
#     best_index = np.nonzero(results['rank_test_%s' % scorer] == 1)[0][0]
#     best_score = results['mean_test_%s' % scorer][best_index]
#
#     # Plot a dotted vertical line at the best score for that scorer marked by x
#     ax.plot([X_axis[best_index], ] * 2, [0, best_score],
#             linestyle='-.', color=color, marker='x', markeredgewidth=3, ms=8)
#
#     # Annotate the best score for that scorer
#     ax.annotate("%0.2f" % best_score,
#                 (X_axis[best_index], best_score + 0.005))
#
# plt.legend(loc="best")
# plt.grid('off')


clf = MLPClassifier(
    # hidden_layer_sizes=int((len(DS_sample[0]) + 2 ) / 2 + 1),
    hidden_layer_sizes=90,
    max_iter=500
)

DS_predict = cross_val_predict(clf, DS_sample, DS_label, cv=10)
conf_matrix = confusion_matrix(DS_label, DS_predict)
# scores = cross_validate(gnb, DS_sample, DS_label, cv=10, scoring=scoring)

print(conf_matrix)
print(classification_report(DS_label, DS_predict))

# plt.show()

