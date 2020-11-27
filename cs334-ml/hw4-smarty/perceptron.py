import argparse
import numpy as np
import pandas as pd
import time


class Perceptron(object):
    mEpoch = 1000  # maximum epoch size
    w = None  # weights of the perceptron

    def __init__(self, epoch):
        self.mEpoch = epoch

    def train(self, xFeat, y):
        """
        Train the perceptron using the data

        Parameters
        ----------
        xFeat : nd-array with shape n x d
            Training data 
        y : 1d array with shape n
            Array of responses associated with training data.

        Returns
        -------
        stats : object
            Keys represent the epochs and values the number of mistakes
        """
        stats = {}
        self.w = np.ones(xFeat.shape[1])

        for i in range(self.mEpoch):
            yHat = self.predict(xFeat)
            for x, y_hat_val, y_val in zip(xFeat, yHat, y):
                if not y_hat_val and y_val:
                    self.w += x
                elif y_hat_val and not y_val:
                    self.w -= x

                m = calc_mistakes(yHat, y)
                stats[i] = m
                if m < 5:
                    break
            if(i == self.mEpoch - 1):
                stats["weights"] = self.w
        return stats

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
        return (np.matmul(self.w, xFeat.T) > 0).astype(int)


def calc_mistakes(yHat, yTrue):
    """
    Calculate the number of mistakes
    that the algorithm makes based on the prediction.

    Parameters
    ----------
    yHat : 1-d array or list with shape n
        The predicted label.
    yTrue : 1-d array or list with shape n
        The true label.      

    Returns
    -------
    err : int
        The number of mistakes that are made
    """
    return np.count_nonzero(np.abs(yHat - yTrue))


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
    parser.add_argument("xTrain",
                        help="filename for features of the training data")
    parser.add_argument("yTrain",
                        help="filename for labels associated with training data")
    parser.add_argument("xTest",
                        help="filename for features of the test data")
    parser.add_argument("yTest",
                        help="filename for labels associated with the test data")
    parser.add_argument("epoch", type=int, help="max number of epochs")
    parser.add_argument("--seed", default=334,
                        type=int, help="default seed number")

    args = parser.parse_args()
    # load the train and test data assumes you'll use numpy
    xTraindf = pd.read_csv(args.xTrain)
    xTrain = xTraindf.to_numpy()
    yTrain = pd.read_csv(args.yTrain)['labels'].to_numpy()
    xTest = pd.read_csv(args.xTest).to_numpy()
    yTest = pd.read_csv(args.yTest)['labels'].to_numpy()

    np.random.seed(args.seed)
    model = Perceptron(args.epoch)
    trainStats = model.train(xTrain, yTrain)
    print(trainStats)

    wordsandweights = sorted([t for t in zip(xTraindf.columns, trainStats['weights'])], key= lambda x: x[1])
    print(wordsandweights[:15])
    print(wordsandweights[-15:])

    yHat = model.predict(xTest)
    # print out the number of mistakes
    print("Number of mistakes on the test dataset")
    print(calc_mistakes(yHat, yTest))


if __name__ == "__main__":
    main()
