# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE
# WRITTEN BY OTHER STUDENTS.
# Simon Marty

import argparse
from typing import List, Any
import pandas as pd
from scipy.spatial.distance import cdist
from numpy import mean


class Knn(object):
    k = 0  # number of neighbors to use
    train_set = None
    train_labels = None

    def __init__(self, k):
        """
        Knn constructor

        Parameters
        ----------
        k : int 
            Number of neighbors to use.
        """
        self.k = k

    def train(self, xFeat: pd.DataFrame, y: pd.DataFrame):
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
        self.train_set = xFeat.copy()
        self.train_labels = y.copy()
        return self

    def predict(self, xFeat: pd.DataFrame) -> List[Any]:
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
        def get_label(row):
            n_smallest = row.nsmallest(self.k).index
            neighbor_labels = self.train_labels.iloc[n_smallest]
            return neighbor_labels.value_counts().idxmax()

        if self.k > xFeat.shape[0] or self.k > self.train_set.shape[0]:
            raise ValueError('k greater than the size of the dataset')

        # Computes the distance between each pair of points in the two dataframes
        # distance_matrix[0] is a list of the distances of the first point of xFeat to every
        # point in self.train_set
        # This is much faster than iteration as we saw before in q1
        # Euclidean is the default distance metric
        distance_matrix = pd.DataFrame(cdist(xFeat, self.train_set))

        # axis=1 applies the function to every row of the DataFrame
        distance_matrix['predicted'] = distance_matrix.apply(get_label, axis=1)

        return distance_matrix['predicted']


def accuracy(yHat: List, yTrue: List):
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
    return mean((yHat == yTrue))




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


if __name__ == "__main__":
    main()
