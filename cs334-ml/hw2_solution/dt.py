import argparse
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import accuracy_score


def partition_data(xFeat, y, splitVar, splitVal):
    # left side will be <= splitVal
    leftIdx = xFeat[splitVar] <= splitVal
    rightIdx = xFeat[splitVar] > splitVal
    return xFeat.loc[leftIdx, :], xFeat.loc[rightIdx], y[leftIdx], y[rightIdx]


def calculate_split_score(y, criterion):
    nTot = len(y)
    # get all the unique values
    classVals = np.unique(y)
    classPor = []
    # tabulate the different portions
    for i in range(len(classVals)):
        classPor.append(float(np.sum(y == classVals[i]))/nTot)
    classPor = np.array(classPor)
    if criterion == "gini":
        return np.sum(np.multiply(classPor, 1-classPor))
    elif criterion == "entropy":
        return -np.sum(np.multiply(classPor, np.log(classPor)))
    else:
        raise Exception("The criterion specified not supported")        


def find_split(xFeat, y, criterion, minLeafSample):
    # go through each feature while keeping track of the best scenario
    # initialize them to the first column + value
    bestSplitVar = xFeat.columns[0]
    bestSplitVal = xFeat.iloc[0, 0]
    bestScore = 1    # set the score to be 1
    for splitVar in xFeat.columns:
        # sort the feature based on the column
        idx = np.argsort(xFeat[splitVar])
        xSorted = xFeat.iloc[idx, :]
        ySorted = y[idx]
        # check all possible splits starting at the min sample
        for i in range(minLeafSample, len(xFeat)-minLeafSample):
            splitVal = xSorted[splitVar].iloc[i]
            # check if the next value is the same as this one
            # if so then just check the next one anyways
            if ySorted[i] == ySorted[i+1]:
                continue
            _, _, yL, yR = partition_data(xSorted,
                                          ySorted,
                                          splitVar,
                                          splitVal)
            sL = calculate_split_score(yL, criterion)
            sR = calculate_split_score(yR, criterion)
            score = float(len(yL) / len(y)) * sL + float(len(yR) / len(y)) * sR
            if score < bestScore:
                # update the split
                bestSplitVar = splitVar
                bestSplitVal = splitVal
                bestScore = score
    return bestSplitVar, bestSplitVal


class DecisionTree(object):
    maxDepth = 0       # maximum depth of the decision tree
    minLeafSample = 0  # minimum number of samples in a leaf
    criterion = None   # splitting criterion
    model = None       # the tree model

    def __init__(self, criterion, maxDepth, minLeafSample):
        """
        decision tree constructor

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

    def is_leaf(self, xFeat, y, depth):
        # if the number of nodes is too small
        if len(y) < self.minLeafSample*2:
            return True
        # check if depth is reached
        elif depth >= self.maxDepth:
            return True
        else:
            return False

    def decision_tree(self, xFeat, y, depth):
        # Stopping criteria
        if self.is_leaf(xFeat, y, depth):  
            return stats.mode(y)[0]
        # find the split
        splitVar, splitVal = find_split(xFeat, y,
                                        self.criterion,
                                        self.minLeafSample)
        # Partition data into two sets
        xL, xR, yL, yR = partition_data(xFeat, y, 
                                        splitVar, splitVal)
        # Recursive call of decision_tree()
        return {"split_variable": splitVar,
                "split_value": splitVal,
                "right": self.decision_tree(xR,
                                            yR,
                                            depth+1), 
                "left": self.decision_tree(xL,
                                           yL,
                                           depth+1)}

    def predict_sample(self, node, x):
        newNode = node['left']
        if x[node['split_variable']] > node['split_value']:
            newNode = node['right']
        # check if it's a dictionary which is another node
        if isinstance(newNode, dict):
            # recursive call of predict_sample
            return self.predict_sample(newNode, x)
        else:
            return newNode

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
        self.model = self.decision_tree(xFeat, y.to_numpy(), 0)
        return self

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
        yHat = [] # variable to store the estimated class label
        # for each node do the prediction
        for i in range(xFeat.shape[0]):
            yHat.append(self.predict_sample(self.model,
                                            xFeat.iloc[i, :]))
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
