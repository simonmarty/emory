import argparse
import numpy as np
import pandas as pd
import seaborn as sns

import knn
from q4 import standard_scale, minmax_range, add_irr_feature
from q4 import knn_train_test


def main():
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

    args = parser.parse_args()
    # load the train and test data
    xTrain = pd.read_csv(args.xTrain)
    yTrain = pd.read_csv(args.yTrain)
    xTest = pd.read_csv(args.xTest)
    yTest = pd.read_csv(args.yTest)
    # set the random number generator
    np.random.seed(100)

    perf = []
    # the different versions of k to try
    for k in range(1, 16, 2):
        acc1 = knn_train_test(k, xTrain, yTrain, xTest, yTest)
        xTrainStd, xTestStd = standard_scale(xTrain, xTest)
        acc2 = knn_train_test(k, xTrainStd, yTrain, xTestStd, yTest)
        xTrainMM, xTestMM = minmax_range(xTrain, xTest)
        acc3 = knn_train_test(k, xTrainMM, yTrain, xTestMM, yTest)
        xTrainIrr, yTrainIrr = add_irr_feature(xTrain, xTest)
        acc4 = knn_train_test(k, xTrainIrr, yTrain, yTrainIrr, yTest)
        perf.append([k, acc1, acc2, acc3, acc4])

    perfDF = pd.DataFrame(perf, columns=["k", "nothing", "std_scale", "minmax", "irr"])

    print(perfDF)
    perfDF = perfDF.set_index("k")
    sns.set(style="whitegrid")
    # also do a plot
    snsPlot = sns.lineplot(data=perfDF,
                            palette="tab10", linewidth=2.5)
    snsfigure = snsPlot.get_figure()    

    snsfigure.savefig("q4d.png")


if __name__ == "__main__":
    main()
