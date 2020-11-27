import argparse
import numpy as np
import pandas as pd
import time
from lr import LinearRegression


class StandardLR(LinearRegression):

    def train_predict(self, xTrain, yTrain, xTest, yTest):
        """
        See definition in LinearRegression class
        """
        start = time.time()
        xTrain['intercepttempcolumn'] = 1
        xTest['intercepttempcolumn'] = 1
        # Computes the vector x that approximately solves the equation ax = b
        # From LAPACK (Fortran), so it's very fast.
        coefs = np.linalg.lstsq(xTrain, yTrain, rcond=None)[0]
        self.beta = coefs.ravel()
        end = time.time() - start
        trainStats = {
            0: {
                "time": end,
                "train-mse": self.mse(xTrain, yTrain['label']),
                "test-mse": self.mse(xTest, yTest['label']),
            }
        }

        return trainStats


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("xTrain",
                        default="eng_xTrain_pruned.csv",
                        help="filename for features of the training data")
    parser.add_argument("yTrain",
                        default="eng_yTrain.csv",
                        help="filename for labels associated with training data")
    parser.add_argument("xTest",
                        default="eng_xTest_pruned.csv",
                        help="filename for features of the test data")
    parser.add_argument("yTest",
                        default="eng_yTest.csv",
                        help="filename for labels associated with the test data")

    args = parser.parse_args()
    # load the train and test data

    xTrain = pd.read_csv(args.xTrain)
    xTest = pd.read_csv(args.xTest)
    yTrain = pd.read_csv(args.yTrain)
    yTest = pd.read_csv(args.yTest)

    model = StandardLR()
    trainStats = model.train_predict(xTrain, yTrain, xTest, yTest)
    print(trainStats)


if __name__ == "__main__":
    main()
