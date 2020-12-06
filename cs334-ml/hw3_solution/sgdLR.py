import argparse
import numpy as np
import pandas as pd
import time

from lr import LinearRegression, file_to_numpy


def grad_pt(beta, xi, yi):
    return np.matmul(np.transpose(xi),(yi-np.matmul(xi, beta)))



class SgdLR(LinearRegression):
    lr = 1  # learning rate
    bs = 1  # batch size
    mEpoch = 1000 # maximum epoch size

    def __init__(self, lr, bs, epoch):
        self.lr = lr
        self.bs = bs
        self.mEpoch = epoch

    def train_predict(self, xTrain, yTrain, xTest, yTest):
        # randomly initialize the weights
        self.beta = np.random.rand(xTrain.shape[1],1)
        # set things up quickly
        trainStats = {}
        n = xTrain.shape[0]
        # get the number of batches
        nBatch = int(float(n) / self.bs)
        startTime = time.time()
        for epoch in range(self.mEpoch):
            # shuffle the dataset
            idx = np.random.permutation(n)
            # iterate through each batch
            for i in range(nBatch):
                bIdx = idx[i*self.bs:(i+1)*self.bs]
                grad = grad_pt(self.beta, xTrain[bIdx], yTrain[bIdx]) / self.bs
                self.beta = self.beta + self.lr*grad
                grad = np.zeros(xTrain.shape[1])
                trainMse = self.mse(xTrain, yTrain)
                testMse = self.mse(xTest, yTest)
                elapsedTime = time.time() - startTime
                trainStats[epoch*nBatch + i] = {'time':elapsedTime,
                                                'train-mse':trainMse,
                                                'test-mse':testMse}
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
    xTrain = file_to_numpy(args.xTrain)
    yTrain = file_to_numpy(args.yTrain)
    xTest = file_to_numpy(args.xTest)
    yTest = file_to_numpy(args.yTest)

    np.random.seed(args.seed)   
    model = SgdLR(args.lr, args.bs, args.epoch)
    trainStats = model.train_predict(xTrain, yTrain, xTest, yTest)
    print(trainStats)



if __name__ == "__main__":
    main()

