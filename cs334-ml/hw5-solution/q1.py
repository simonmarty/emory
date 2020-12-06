import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.decomposition as skd
import sklearn.linear_model as sklm
import sklearn.metrics as skm
import sklearn.preprocessing as skp


def normalize_feat(xTrain, xTest):
    """
    Normalize xTrain and xTest
    """
    stdScaler = skp.StandardScaler()
    stdScaler.fit(xTrain)
    return stdScaler.transform(xTrain), stdScaler.transform(xTest)


def unreg_log(xTrain, yTrain, xTest, yTest):
    logR = sklm.LogisticRegression(penalty='none',
                                   solver='saga',
                                   max_iter=10000)
    logR.fit(xTrain, yTrain)
    # predict the probabilities
    yHat = logR.predict_proba(xTest)
    # calculate the ROC
    fpr, tpr, _ = skm.roc_curve(yTest, yHat[:, 1])
    return fpr, tpr


def run_pca(xTrain, xTest):
    # set the shape to be the max
    pcaModel = skd.PCA(n_components=xTrain.shape[1])
    pcaModel.fit(xTrain)
    # calculate number of components to get to 95%
    expVar = pcaModel.explained_variance_ratio_
    totVar = np.cumsum(expVar)
    k = np.argmax(totVar > 0.95) + 1
    # refit it to this value
    pcaModel = skd.PCA(n_components=k)
    pcaModel.fit(xTrain)
    return pcaModel.transform(xTrain), pcaModel.transform(xTest), pcaModel.components_


def run_nmf(xTrain, xTest, approxTol=1):
    maxK = np.max(xTrain.shape[1])
    lastErr = np.finfo(float).max
    for k in range(1, maxK, 1):
        nmfModel = skd.NMF(n_components=k)
        nmfModel.fit(xTrain)
        err = nmfModel.reconstruction_err_
        if lastErr - err < approxTol or err < approxTol:
            break
        lastErr = err
    return nmfModel.transform(xTrain), nmfModel.transform(xTest), nmfModel.components_


def file_to_numpy(filename):
    """
    Read an input file and convert it to numpy
    """
    df = pd.read_csv(filename)
    return df.to_numpy(), df.columns


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
    xTrain, feats = file_to_numpy(args.xTrain)
    yTrain, _ = file_to_numpy(args.yTrain)
    # unravel it to make it work
    yTrain = yTrain.ravel()
    xTest, _ = file_to_numpy(args.xTest)
    yTest, _ = file_to_numpy(args.yTest)
    yTest = yTest.ravel()
    fpr = [None]*3
    tpr = [None]*3
    # normalize the features
    nxTrain, nxTest = normalize_feat(xTrain, xTest)
    fpr[0], tpr[0] = unreg_log(nxTrain, yTrain, nxTest, yTest)
    # run pca and train another logistic regression
    pcaTrain, pcaTest, pcaComp = run_pca(nxTrain, nxTest)
    pcaDF = pd.DataFrame(pcaComp, columns=feats)
    pcaDF.to_csv("pcaComps.csv")
    fpr[1], tpr[1] = unreg_log(pcaTrain, yTrain, pcaTest, yTest)
    # run nmf and train the last one
    nmfTrain, nmfTest, nmfComp = run_nmf(xTrain, xTest)
    nmfComp = pd.DataFrame(nmfComp, columns=feats)
    nmfComp.to_csv("nmfComp.csv")
    fpr[2], tpr[2] = unreg_log(nmfTrain, yTrain, nmfTest, yTest)

    # plot the ROC part
    colors = ['aqua', 'darkorange', 'cornflowerblue']
    labelList = ['none', 'PCA', 'NMF']
    plt.figure()
    for i, color in zip(range(3), colors):
        plt.plot(fpr[i], tpr[i], color=color,
                 lw=2,
                 label=labelList[i])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Q1')
    plt.legend(loc="lower right")
    plt.savefig('q1.png')


if __name__ == "__main__":
    main()
