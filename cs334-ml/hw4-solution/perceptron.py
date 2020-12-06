import argparse
import numpy as np
import pandas as pd
import time

class Perceptron(object):
    mEpoch = 1000  # maximum epoch size
    w = None       # weights of the perceptron

    def __init__(self, epoch):
        self.mEpoch = epoch
        self.lrate = 1
        self.w = None

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
        # TODO implement this
        self.w = np.zeros(xFeat.shape[1]+1)
        for i in range(self.mEpoch):
        	errs = 0
        	for datx, label in zip(xFeat, y):
        		prediction = self.predicts(datx)
        		self.w[1:]+= self.lrate * (label - prediction) *datx
        		self.w[0]+= self.lrate * (label - prediction)
        		errs  += np.abs(label[0]-prediction)
        	if errs==0:
        		stats[i+1]={'Mistakes': 0}
        		return stats
        	stats[i+1] ={'Mistakes': errs} 
        return stats 

    def predicts(self, xFeat):
        yHat = []
        re = self.w[0]+np.dot(xFeat, self.w[1:])
        if re >= 0:
        	result = 1
        else:
        	result = 0
        yHat = result
        return yHat
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
    	yHat = []
    	res = self.w[0]+np.dot(xFeat, self.w[1:])
    	res = np.sign(res)
    	res[res<=0] = 0
    	yHat = res
    	return yHat


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
    mistake = 0
    for i in range(len(yHat)):
    	if yHat[i] != yTrue[i]:
    		mistake +=1
    return mistake


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
    parser.add_argument("epoch", type=int, help="max number of epochs")
    parser.add_argument("--xTrain",
    					default="BinaryXTrain.csv",
                        help="filename for features of the training data")
    parser.add_argument("--yTrain",
    					default="yTrain.csv",
                        help="filename for labels associated with training data")
    parser.add_argument("--xTest",
    					default="BinaryXTest.csv",
                        help="filename for features of the test data")
    parser.add_argument("--yTest",
    					default="yTest.csv",
                        help="filename for labels associated with the test data")
    
    parser.add_argument("--seed", default=334, 
                        type=int, help="default seed number")
    
    args = parser.parse_args()
    # load the train and test data assumes you'll use numpy
    xTrain = file_to_numpy(args.xTrain)
    yTrain = file_to_numpy(args.yTrain)
    xTest = file_to_numpy(args.xTest)
    yTest = file_to_numpy(args.yTest)

    np.random.seed(args.seed)   
    model = Perceptron(args.epoch)
    trainStats = model.train(xTrain, yTrain)
    print(trainStats)
    yHat = model.predict(xTest)
    # print out the number of mistakes
    print("Number of mistakes on the test dataset")
    print(calc_mistakes(yHat, yTest))


if __name__ == "__main__":
    main()