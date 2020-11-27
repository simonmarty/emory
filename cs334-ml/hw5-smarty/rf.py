import argparse
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from scipy.stats import mode


class RandomForest:
    nest = 0  # number of trees
    maxFeat = 0  # maximum number of features
    maxDepth = 0  # maximum depth of the decision tree
    minLeafSample = 0  # minimum number of samples in a leaf
    criterion = None  # splitting criterion
    forest = None

    def __init__(self, nest=40, maxFeat=6, criterion="gini", maxDepth=None, minLeafSample=1):
        """
        Decision tree constructor

        Parameters
        ----------
        nest: int
            Number of trees to have in the forest
        maxFeat: int
            Maximum number of features to consider in each tree
        criterion : String
            The function to measure the quality of a split.
            Supported criteria are "gini" for the Gini impurity
            and "entropy" for the information gain.
        maxDepth : int 
            Maximum depth of the decision tree
        minLeafSample : int 
            Minimum number of samples in the decision tree
        """
        self.nest = nest
        self.maxFeat = maxFeat
        self.criterion = criterion
        self.maxDepth = maxDepth
        self.minLeafSample = minLeafSample
        self.forest = [
            DecisionTreeClassifier(criterion=self.criterion,
                                   max_depth=self.maxDepth,
                                   min_samples_leaf=self.minLeafSample)
            for _ in range(self.nest)
        ]
        self.attributes_selected = []
        self.oob = []

    def train(self, xFeat, y):
        """
        Train the random forest using the data

        Parameters
        ----------
        xFeat : pd.DataFrame with shape n x d
            Training data 
        y : 1d array with shape n
            Array of responses associated with training data.

        Returns
        -------
        stats : object
            Keys represent the number of trees and
            the values are the out of bag errors
        """
        for tree in self.forest:
            column_sample = np.random.choice(xFeat.shape[1], size=self.maxFeat, replace=False)
            row_sample = np.random.choice(xFeat.shape[0], size=xFeat.shape[0], replace=True)
            complement = np.array([i for i in range(xFeat.shape[0]) if i not in row_sample])
            self.oob.append(complement)
            self.attributes_selected.append(column_sample)
            tree.fit(xFeat[row_sample[:, None], column_sample], y)
        return self.calc_oob(xFeat)

    def calc_oob(self, xFeat):
        oob_error = []
        for i, tree in enumerate(self.forest):
            oob_rows = xFeat[self.oob[i], :]
            tree_output = []
            for j, other_tree in enumerate(self.forest):
                # Pass if same tree
                if i == j:
                    continue
                # Predict with the same parameters it was trained with
                tree_output.append(other_tree.predict(oob_rows[:, self.attributes_selected[j]]))
            tree_output = mode(np.transpose(tree_output), axis=1)[0].ravel()
            predictions = tree.predict(oob_rows[:, self.attributes_selected[i]])
            oob_error.append(np.sum(tree_output != predictions) / oob_rows.shape[0])
        return oob_error

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
            Predicted response per sample
        """
        tree_output = []
        for i, tree in enumerate(self.forest):
            tree_output.append(tree.predict(xFeat[:, self.attributes_selected[i]]))
        return mode(np.transpose(tree_output), axis=1)[0].ravel()


def file_to_numpy(filename):
    """
    Read an input file and convert it to numpy
    """
    df = pd.read_csv(filename)
    return df.to_numpy()


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--xTrain", default="q4xTrain.csv",
                        help="filename for features of the training data")
    parser.add_argument("--yTrain", default="q4yTrain.csv",
                        help="filename for labels associated with training data")
    parser.add_argument("--xTest", default="q4xTest.csv",
                        help="filename for features of the test data")
    parser.add_argument("--yTest", default="q4yTest.csv",
                        help="filename for labels associated with the test data")
    parser.add_argument("--epoch", default=2, type=int,
                        help="max number of epochs")
    parser.add_argument("--seed", default=334,
                        type=int, help="default seed number")

    args = parser.parse_args()

    xTrain = file_to_numpy(args.xTrain)
    yTrain = file_to_numpy(args.yTrain)
    xTest = file_to_numpy(args.xTest)
    yTest = file_to_numpy(args.yTest)

    np.random.seed(args.seed)
    model = RandomForest(args.epoch)
    trainStats = model.train(xTrain, yTrain)
    print(trainStats)
    yHat = model.predict(xTest)
    print(np.sum(yHat == yTest.ravel()) / yTest.ravel().shape[0])


if __name__ == "__main__":
    main()
