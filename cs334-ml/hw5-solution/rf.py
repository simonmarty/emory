import argparse
import collections
import numpy as np
import pandas as pd
import sklearn.metrics as skm
import sklearn.tree as skt

class RandomForest(object):
    nest = 0           # number of trees
    maxFeat = 0        # maximum number of features
    maxDepth = 0       # maximum depth of the decision tree
    minLeafSample = 0  # minimum number of samples in a leaf
    criterion = None   # splitting criterion
    model = {}         # keeping track of all the models developed

    def __init__(self, nest, maxFeat, criterion, maxDepth, minLeafSample):
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
        self.criterion = criterion
        self.maxFeat = maxFeat
        self.maxDepth = maxDepth
        self.minLeafSample = minLeafSample

    def train(self, xFeat, y):
        """
        Train the random forest using the data

        Parameters
        ----------
        xFeat : nd-array with shape n x d
            Training data 
        y : 1d array with shape n
            Array of responses associated with training data.

        Returns
        -------
        stats : object
            Keys represent the number of trees and
            the values are the out of bag errors
        """
        n = xFeat.shape[0]
        d = xFeat.shape[1]
        nArr = range(n)
        oobPredict = collections.defaultdict(list)
        oobErr = {}
        # iterate through the m trees
        for m in range(self.nest):
            # bootstrap indices
            trainIdx = np.random.choice(nArr, n, replace=True)
            # get those that are oob
            oobIdx = np.setdiff1d(nArr, trainIdx)
            # get the feature idx
            featIdx = np.random.choice(d, self.maxFeat, replace=False)
            # subset the bootstrap data
            xTemp = xFeat[trainIdx][:, featIdx]
            yTemp = y[trainIdx]
            # train the model and store the stuff
            self.model[m] = {"tree": skt.DecisionTreeClassifier(criterion=self.criterion,
                                    max_depth=self.maxDepth,
                                    min_samples_leaf=self.minLeafSample),
                        "feat": featIdx,
                        "oob": oobIdx}
            self.model[m]["tree"].fit(xTemp, yTemp)
            # predict the OOB
            xOob = xFeat[oobIdx][:, featIdx]
            yOob = self.model[m]["tree"].predict(xOob)
            for k, idx in enumerate(oobIdx):
                oobPredict[idx].append(yOob[k])
            # predict all OOB
            oobHat = {k: ((np.sum(v)/ len(v)) >= 0.5)*1 for k, v in oobPredict.items()}
            # calculate errors
            oobErr[m] = 1-skm.accuracy_score(y[list(oobHat.keys())],
                                             list(oobHat.values()))
        return oobErr

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
        yHat = np.zeros(xFeat.shape[0])
        for m in range(self.nest):
            xTemp = xFeat[:, self.model[m]["feat"]]
            yHat = yHat + self.model[m]["tree"].predict(xTemp)
        yHat = (yHat > m/2) * 1
        return yHat


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
    parser.add_argument("n", type=int, help="number of trees")
    parser.add_argument("mf",
                        type=int,
                        help="maximum number of features")
    parser.add_argument("md",
                        type=int,
                        help="maximum depth")
    parser.add_argument("mls",
                        type=int,
                        help="minimum leaf samples")
    parser.add_argument("--seed", default=334, 
                        type=int, help="default seed number")
    
    args = parser.parse_args()
    # load the train and test data assumes you'll use numpy
    xTrain = file_to_numpy(args.xTrain)
    yTrain = file_to_numpy(args.yTrain)
    yTrain = yTrain.ravel()
    xTest = file_to_numpy(args.xTest)
    yTest = file_to_numpy(args.yTest)

    np.random.seed(args.seed)   
    model = RandomForest(args.n, args.mf, 'gini', args.md, args.mls)
    trainStats = model.train(xTrain, yTrain)
    print(trainStats)
    yHat = model.predict(xTest)


if __name__ == "__main__":
    main()