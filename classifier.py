from argparse import ArgumentParser
import csv
import pydotplus
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
def read_csv_file(file_name):
    with open(file_name) as file:
        rows = np.array(list(csv.reader(file)))
    return rows[0, :-1], rows[0, -1], rows[1:][:, [0, -2]], rows[1:][:, [-1]]
parser = ArgumentParser()
parser.add_argument("input", help = "the input csv file")
parser.add_argument("-c", "--classifier", help = "the classifier", default = "0", dest = "classifier")
parser.add_argument("-t", "--test", help = "the csv file used to test accuracy", default = None, dest = "test")
parser.add_argument("-o", "--output", help = "the output png file of the rule of decision tree", default = None, dest = "output")
args = parser.parse_args()
title_x, title_y, x, y = read_csv_file(args.input)
if args.classifier == "0":
    clf = DecisionTreeClassifier()
elif args.classifier == "1":
    clf = RandomForestClassifier()
clf.fit(x, y)
if not args.test == None:
    test_title_x, test_title_y, test_x, test_y = read_csv_file(args.test)
    predict_y = clf.predict(test_x)
    accuracy = accuracy_score(test_y, predict_y)
    print "accuracy:", accuracy
if not args.output == None:
    dot_data = export_graphviz(clf, feature_names = title_x, out_file = None, filled = True, rounded = True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png(args.output)
xx, yy = np.meshgrid(np.arange(0, 1, 0.01), np.arange(0, 1, 0.01))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.subplots(1, 1, figsize = (4, 4))
plt.xlabel(title_x[0])
plt.ylabel(title_x[1])
plt.contourf(xx, yy, Z, cmap = plt.cm.Paired)
plt.show()
