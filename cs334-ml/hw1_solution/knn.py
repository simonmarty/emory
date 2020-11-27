import argparse
import numpy as np
import pandas as pd

from sklearn import neighbors
import sklearn


class Knn(object):
    k = 0         # number of neighbors to use
    xFeat = None  # add storage of the features
    y = None      # add storage of the labels

    def __init__(self, k):
        """
        Knn constructor

        Parameters
        ----------
        k : int 
            Number of neighbors to use.
        """
        self.k = k

    def train(self, xFeat, y):
        """
        Train the k-nn model.

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
        # store the two objects
        if isinstance(xFeat, pd.DataFrame):
            xFeat = xFeat.to_numpy()
        self.xFeat = xFeat
        self.y = y
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
        # convert to numpy for ease
        if isinstance(xFeat, pd.DataFrame):
            xFeat = xFeat.to_numpy()
        # for each sample of the row
        for i in range(xFeat.shape[0]):
            # apply the euclidean distance which is just the 2-norm
            dist = np.linalg.norm(self.xFeat - xFeat[i, :], axis=1)
            # an equivalent way to do this would be:
            # tmp = (self.xFeat - xFeat[i, :])**2
            # dist = np.sqrt(np.sum(tmp, axis=1))
            # do an argument sort
            idx = np.argsort(dist)
            # get the labels for the first k
            yNeighbors = self.y.iloc[idx[0:self.k]]
            yHat.append(yNeighbors.mode()[0])
        return yHat


def accuracy(yHat, yTrue):
    """
    Calculate the accuracy of the prediction

    Parameters
    ----------
    yHat : 1d-array with shape n
        Predicted class label for n samples
    yTrue : 1d-array with shape n
        True labels associated with the n samples

    Returns
    -------
    acc : float between [0,1]
        The accuracy of the model
    """
    # TODO calculate the accuracy
    acc = np.sum(yHat == yTrue) / len(yTrue)
    return acc


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("k",
                        type=int,
                        help="the number of neighbors")
    parser.add_argument("--xTrain",
                        default="q3xTrain.csv",
                        help="filename for features of the training data")
    parser.add_argument("--yTrain",
                        default="q3yTrain.csv",
                        help="filename for labels associated with training data")
    parser.add_argument("--xTest",
                        default="q3xTest.csv",
                        help="filename for features of the test data")
    parser.add_argument("--yTest",
                        default="q3yTest.csv",
                        help="filename for labels associated with the test data")

    args = parser.parse_args()
    # load the train and test data
    xTrain = pd.read_csv(args.xTrain)
    yTrain = pd.read_csv(args.yTrain)
    xTest = pd.read_csv(args.xTest)
    yTest = pd.read_csv(args.yTest)
    # create an instance of the model
    knn = Knn(args.k)
    knn.train(xTrain, yTrain['label'])
    # predict the training dataset
    yHatTrain = knn.predict(xTrain)
    trainAcc = accuracy(yHatTrain, yTrain['label'])
    # predict the test dataset
    yHatTest = knn.predict(xTest)
    testAcc = accuracy(yHatTest, yTest['label'])
    print("Training Acc:", trainAcc)
    print("Test Acc:", testAcc)

    # This is a sanity check and not in the original file
    knn = neighbors.KNeighborsClassifier(args.k)
    knn.fit(xTrain, yTrain['label'])
    yHatTrain = knn.predict(xTrain)
    yHatTest = knn.predict(xTest)
    trainAcc = sklearn.metrics.accuracy_score(yTrain['label'], yHatTrain)
    testAcc = sklearn.metrics.accuracy_score(yTest['label'], yHatTest)
    print("sklearn - Training Acc:", trainAcc)
    print("sklearn - Test Acc:", testAcc)

if __name__ == "__main__":
    main()
