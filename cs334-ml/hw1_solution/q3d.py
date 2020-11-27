import argparse
import numpy as np
import pandas as pd
import seaborn as sns

import knn


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
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

    perf = []
    # the different versions of k to try
    for k in range(1, 20, 2):
        model = knn.Knn(k)
        model.train(xTrain, yTrain['label'])
        yHatTrain = model.predict(xTrain)
        trainAcc = knn.accuracy(yHatTrain, yTrain['label'])
        yHatTest = model.predict(xTest)
        testAcc = knn.accuracy(yHatTest, yTest['label'])
        perf.append([k, trainAcc, testAcc])

    perfDF = pd.DataFrame(perf, columns=["k", "train", "test"])
    print(perfDF)
    perfDF = perfDF.set_index("k")
    sns.set(style="whitegrid")
    # also do a plot
    snsPlot = sns.lineplot(data=perfDF,
                            palette="tab10", linewidth=2.5)
    snsfigure = snsPlot.get_figure()    

    snsfigure.savefig("q3d.png")

if __name__ == "__main__":
    main()
