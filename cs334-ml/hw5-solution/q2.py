import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.metrics as skm

from rf import RandomForest, load_dataset


def search_param(xTrain, yTrain, xTest, yTest):
    perf = pd.DataFrame()
    # do a grid search using OOB and set max trees to 250
    for crit in ['gini', 'entropy']:
        for mf in range(5,12):
            for md in range(1,6):
                for mls in range(5,8):
                    print(crit, mf, md, mls)
                    rf = RandomForest(250, mf,
                                      crit, md,
                                      mls)
                    oobErr = rf.train(xTrain, yTrain)
                    # use oob to keep track of stuff
                    tmpDF = pd.DataFrame.from_dict(oobErr,
                                                   orient='index',
                                                   columns=['err'])
                    tmpDF['nest'] = tmpDF.index
                    tmpDF['crit'] = crit
                    tmpDF['mf'] = mf
                    tmpDF['md'] = md
                    tmpDF['mls'] = mls
                    perf = pd.concat([perf, tmpDF])
    # clean up the indexing for the pandas dataframe
    perf = perf.reset_index(drop=True)
    return perf


def eval_opt(xTrain, yTrain, xTest, yTest):
    bst = RandomForest(47, 7, 'gini', 4, 5)
    ypred = bst.predict(xTest)
    # evaluate predictions
    print(1-skm.accuracy_score(yTest, ypred))


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
    xTrain, yTrain, xTest, yTest = load_dataset(args.xTrain,
                                                args.yTrain,
                                                args.xTest,
                                                args.yTest)
    perf = search_param(xTrain, yTrain, xTest, yTest)
    # since OOB may not be stable for the first few
    # we'll remove any nest < 5
    perf = perf[perf['nest'] >= 5]
    # figure out the minimum from all the values for each one
    idx = perf.groupby(['crit', 'mf', 'md', 'mls'])['err'].idxmin()
    bestPerf = perf.loc[idx]
    print(bestPerf.sort_values(by='err')[1:50].to_latex(index=False))
    eval_opt(xTrain, yTrain, xTest, yTest)

if __name__ == "__main__":
    main()
