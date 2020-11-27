import argparse

import numpy as np
import pandas as pd
from scipy.stats import entropy
from sklearn.metrics import accuracy_score
from collections import Counter
import numpy as np


def split_data(attribute, split, df):
    right = df[df[attribute] >= split]
    left = df[df[attribute] < split]
    return left, right


def gini_coefficient(x):

    c = Counter(x)

    return sum([(i/len(x))*(1-(i/len(x))) for i in c])


def entropy(x):
    c = Counter(x)
    return sum([(-i / len(x)) * np.log2(i / len(x)) for i in c.values()])


def search_split(attribute, data, criterion):
    attr = data[attribute].to_numpy()
    y = data['class'].to_numpy()
    res = []
    i = 0
    for j in range(len(attr)):
        if y[j] != i:
            i = y[j]
            res.append((attr[j] + attr[j - 1]) / 2)
    costs = {}

    for v in res:
        left, right = split_data(attribute, v, data)

        if criterion == 'entropy':
            critfunc = entropy
        else:
            critfunc = gini_coefficient

        left_cost = critfunc(left['class'])
        right_cost = critfunc(right['class'])

        costs[v] = (right_cost * len(right)
                    + left_cost * len(left)) / (len(right) + len(left))

    split = min(costs, key=costs.get)
    return costs[split], split


def get_best_feature(data, criterion):
    df = data.columns[:-1]
    costs, splits = {}, {}
    for e in df:
        costs[e], splits[e] = search_split(e, data, criterion)
    k = min(costs, key=costs.get)
    return k, splits[k]


class Node:
    def __init__(self, depth, attribute=None, split=None,
                 left=None, right=None, leaf=False, classification=None):
        self.depth = depth
        self.attribute = attribute
        self.split = split
        self.left = left
        self.right = right
        self.leaf = leaf
        self.classification = classification

    def choose(self, v):
        return self.split < v


class DecisionTree(object):
    maxDepth = 0  # maximum depth of the decision tree
    minLeafSample = 0  # minimum number of samples in a leaf
    criterion = None  # splitting criterion

    def __init__(self, criterion, maxDepth, minLeafSample):
        """
        Decision tree constructor

        Parameters
        ----------
        criterion : String
            The function to measure the quality of a split.
            Supported criteria are "gini" for the Gini impurity
            and "entropy" for the information gain.
        maxDepth : int 
            Maximum depth of the decision tree
        minLeafSample : int 
            Minimum number of samples in the decision tree
        """
        self.criterion = criterion
        self.maxDepth = maxDepth
        self.minLeafSample = minLeafSample
        self.data = None
        self.root = None

    def train(self, xFeat, y):
        """
        Train the decision tree model.

        Parameters
        ----------
        xFeat : nd-array with shape n x d
            Training data 
        y : 1d array with shape n
            Array of labels associated with training data.

        Returns
        -------
        self : object
        """
        self.data = pd.DataFrame(xFeat)
        self.data['class'] = y
        self.root = self.fit(self.data, 0)
        return self

    def fit(self, data, depth):
        if depth > self.maxDepth:
            return

        y = data['class']

        if len(y) >= self.minLeafSample and len(set(y)) > 1 and depth < self.maxDepth:
            attribute, split = get_best_feature(data, self.criterion)
            left, right = split_data(attribute, split, data)
            n = Node(attribute=attribute, split=split, left=self.fit(
                left, depth + 1), right=self.fit(right, depth + 1), depth=depth)
        else:
            y2 = list(y)
            n = Node(leaf=True, classification=max(y2, key=y2.count), depth=depth)
        return n

    def predict(self, xFeat):
        """
        Given the feature set xFeat, predict 
        what class the values will have.

        Parameters
        ----------
        xFeat : nd-array with shape m x d
            The data to predict.  

        Returns
        -------
        yHat : 1d array or list with shape m
            Predicted class label per sample
        """
        yHat = []  # variable to store the estimated class label

        for i, v in xFeat.iterrows():
            node = self.root
            while not node.leaf:
                if node.choose(v[node.attribute]):
                    node = node.right
                else:
                    node = node.left
            yHat.append(node.classification)
        return yHat


def dt_train_test(dt, xTrain, yTrain, xTest, yTest):
    """
    Given a decision tree model, train the model and predict
    the labels of the test data. Returns the accuracy of
    the resulting model.

    Parameters
    ----------
    dt : DecisionTree
        The decision tree with the model parameters
    xTrain : nd-array with shape n x d
        Training data 
    yTrain : 1d array with shape n
        Array of labels associated with training data.
    xTest : nd-array with shape m x d
        Test data 
    yTest : 1d array with shape m
        Array of labels associated with test data.

    Returns
    -------
    acc : float
        The accuracy of the trained knn model on the test data
    """
    # train the model
    dt.train(xTrain, yTrain['label'])
    # predict the training dataset
    yHatTrain = dt.predict(xTrain)
    trainAcc = accuracy_score(yTrain['label'], yHatTrain)
    # predict the test dataset
    yHatTest = dt.predict(xTest)
    testAcc = accuracy_score(yTest['label'], yHatTest)
    return trainAcc, testAcc


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("md",
                        type=int,
                        help="maximum depth")
    parser.add_argument("mls",
                        type=int,
                        help="minimum leaf samples")
    parser.add_argument("--xTrain",
                        default="q4xTrain.csv",
                        help="filename for features of the training data")
    parser.add_argument("--yTrain",
                        default="q4yTrain.csv",
                        help="filename for labels associated with training data")
    parser.add_argument("--xTest",
                        default="q4xTest.csv",
                        help="filename for features of the test data")
    parser.add_argument("--yTest",
                        default="q4yTest.csv",
                        help="filename for labels associated with the test data")

    args = parser.parse_args()
    # load the train and test data
    xTrain = pd.read_csv(args.xTrain)
    yTrain = pd.read_csv(args.yTrain)
    xTest = pd.read_csv(args.xTest)
    yTest = pd.read_csv(args.yTest)
    # create an instance of the decision tree using gini
    dt1 = DecisionTree('gini', args.md, args.mls)
    trainAcc1, testAcc1 = dt_train_test(dt1, xTrain, yTrain, xTest, yTest)
    print("GINI Criterion ---------------")
    print("Training Acc:", trainAcc1)
    print("Test Acc:", testAcc1)
    dt = DecisionTree('entropy', args.md, args.mls)
    trainAcc, testAcc = dt_train_test(dt, xTrain, yTrain, xTest, yTest)
    print("Entropy Criterion ---------------")
    print("Training Acc:", trainAcc)
    print("Test Acc:", testAcc)


if __name__ == "__main__":
    main()
