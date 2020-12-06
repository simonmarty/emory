import argparse
import numpy as np
import pandas as pd
import time

from lr import LinearRegression, file_to_numpy


class StandardLR(LinearRegression):

    def train_predict(self, xTrain, yTrain, xTest, yTest):
        """
        See definition in LinearRegression class
        """
        trainStats = {}
        startTime = time.time()
        temp = np.ones((len(xTrain),1), dtype=int)
        Int = np.ones((len(xTest),1),dtype = int)
        xTest = np.concatenate((xTest,Int),axis =1)
        xTrain = np.concatenate((xTrain, temp), axis=1)
        xt = np.transpose(xTrain)
        # calculate (X^T)X
        xtx = np.matmul(xt, xTrain)
        # calculate the inverse of xtx
        xtxi = np.linalg.inv(xtx)
        # xty
        xty = np.matmul(xt, yTrain)
        self.beta = np.matmul(xtxi, xty)
        trainMse = self.mse(xTrain, yTrain)
        testMse = self.mse(xTest, yTest)
        elapsedTime = time.time() - startTime
        trainStats[0] = {'time': elapsedTime,
                         'train-mse': trainMse,
                         'test-mse': testMse}
        return trainStats


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("xTrain",
                        help="filename for features of the training data")
    parser.add_argument("yTrain",
                        help="filename for labels associated with training data")
    parser.add_argument("xTest",
                        help="filename for features of the test data")
    parser.add_argument("yTest",
                        help="filename for labels associated with the test data")

    args = parser.parse_args()
    # load the train and test data
    xTrain = file_to_numpy(args.xTrain)
    yTrain = file_to_numpy(args.yTrain)
    xTest = file_to_numpy(args.xTest)
    yTest = file_to_numpy(args.yTest)

    model = StandardLR()
    trainStats = model.train_predict(xTrain, yTrain, xTest, yTest)
    print(trainStats)


if __name__ == "__main__":
    main()
