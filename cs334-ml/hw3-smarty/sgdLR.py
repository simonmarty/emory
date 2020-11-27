import argparse
import numpy as np
import time

from lr import LinearRegression, to_numpy


class SgdLR(LinearRegression):
    lr = 1  # learning rate
    bs = 1  # batch size
    mEpoch = 1000  # maximum epoch size

    def __init__(self, lr, bs, epoch):
        self.lr = lr
        self.bs = bs
        self.mEpoch = epoch

    def new_batch(self, x, y):
        for i in np.arange(0, x.shape[0], self.bs):
            # Generator, supplies one batch at a time
            yield x[i:i + self.bs], y[i:i + self.bs]

    def train_predict(self, xTrain, yTrain, xTest, yTest):
        """
        See definition in LinearRegression class
        """
        trainStats = {}
        xTrain = np.c_[np.ones((xTrain.shape[0])), xTrain]
        xTest = np.c_[np.ones((xTest.shape[0])), xTest]
        yTrain = yTrain.ravel()
        yTest = yTest.ravel()

        self.beta = np.random.uniform(size=(xTrain.shape[1],))

        for i in range(self.mEpoch):
            for j, (batch_x, batch_y) in enumerate(self.new_batch(xTrain, yTrain)):
                start = time.time()
                self.beta += self.lr * \
                    batch_x.T.dot(batch_y - batch_x.dot(self.beta)
                                  ) / batch_x.shape[0]
                end = time.time() - start
                trainStats[i + j] = {
                    "time": end,
                    "train-mse": self.mse(xTrain, yTrain),
                    "test-mse": self.mse(xTest, yTest),
                }

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
    parser.add_argument("lr", type=float, help="learning rate")
    parser.add_argument("bs", type=int, help="batch size")
    parser.add_argument("epoch", type=int, help="max number of epochs")
    parser.add_argument("--seed", default=334,
                        type=int, help="default seed number")

    args = parser.parse_args()
    # load the train and test data
    xTrain = to_numpy(args.xTrain)
    yTrain = to_numpy(args.yTrain)
    xTest = to_numpy(args.xTest)
    yTest = to_numpy(args.yTest)

    # setting the seed for deterministic behavior
    np.random.seed(args.seed)
    model = SgdLR(args.lr, args.bs, args.epoch)
    trainStats = model.train_predict(xTrain, yTrain, xTest, yTest)
    print(trainStats)


if __name__ == "__main__":
    main()
