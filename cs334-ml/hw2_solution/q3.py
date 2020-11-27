import argparse
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection as skms


KNN_PARAMETERS = {'n_neighbors' : range(1,16,2)}
DT_PARAMETERS = {'min_samples_leaf' : range(5,20,5),
                 'max_depth': range(3,10,2),
                 'criterion': ['gini', 'entropy']}


def model_opt(model, modelParams,
              xTrain, yTrain,
              xTest, yTest):
    gs = skms.GridSearchCV(model,
                       modelParams,
                       cv=5,
                       scoring='roc_auc')  
    gsResult = gs.fit(xTrain, yTrain)
    print(gsResult.best_params_)
    nTrain = len(xTrain)
    robustStats = {}
    for rRate in [0, 0.05, 0.1, 0.2]:
        # take a subset of the samples
        nNew = int(nTrain*(1-rRate))
        newIdx = np.random.choice(nTrain, nNew, replace=False)
        xTrainNew = xTrain.iloc[newIdx, :]
        yTrainNew = yTrain[newIdx]
        # train and test
        perf = train_test(gsResult.best_estimator_,
                          xTrainNew, yTrainNew,
                          xTest, yTest)
        robustStats[rRate] = perf
    return pd.DataFrame(robustStats)


def train_test(model, xTrain, yTrain, xTest, yTest):
    """
    Given a sklearn train/test calculate the auc
    """
    # fit the data to the training dataset
    model.fit(xTrain, yTrain)
    # predict training and testing probabilties
    yHatTrain = model.predict_proba(xTrain)
    yHatTest = model.predict_proba(xTest)
    # calculate auc for training
    fpr, tpr, thresholds = metrics.roc_curve(yTrain,
                                             yHatTrain[:, 1])
    trainAuc = metrics.auc(fpr, tpr)
    # calculate auc for test dataset
    fpr, tpr, thresholds = metrics.roc_curve(yTest,
                                             yHatTest[:, 1])
    testAuc = metrics.auc(fpr, tpr)
    yHatClassTrain = model.predict(xTrain)
    yHatClassTest = model.predict(xTest)
    return {"trainAuc": trainAuc,
            "testAuc": testAuc,
            "trainAcc": metrics.accuracy_score(yTrain,
                                               yHatClassTrain),
            "testAcc": metrics.accuracy_score(yTest,
                                              yHatClassTest)}



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
    # convert it to a flattened array
    yTrain = yTrain.to_numpy().flatten()
    xTest = pd.read_csv(args.xTest)
    yTest = pd.read_csv(args.yTest)
    yTest = yTest.to_numpy().flatten()

    print("KNN Results---------")
    print(model_opt(KNeighborsClassifier(),
                    KNN_PARAMETERS,
                    xTrain, yTrain,
                    xTest, yTest))
    print("DT Results---------")
    print(model_opt(DecisionTreeClassifier(),
                    DT_PARAMETERS,
                    xTrain, yTrain,
                    xTest, yTest))
   

if __name__ == "__main__":
    main()
