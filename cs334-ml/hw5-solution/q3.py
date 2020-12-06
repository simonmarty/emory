import sklearn.metrics as skm
import xgboost as xgb

from rf import load_dataset


def search_params(dtrain):
    perf = pd.DataFrame()
    for md in range(3, 10):
        for lr in [0.001, 0.01, 0.1, 0.5, 1]:
            param = {'max_depth': md,
                     'eta': lr,
                     'objective':'binary:logistic'}
            res = xgb.cv(param, dtrain, 200, nfold=5,
                   metrics={'error'}, seed=334)
            tmpDF = pd.DataFrame(res)
            tmpDF['it'] = tmpDF.index
            tmpDF['md'] = md
            tmpDF['lr'] = lr
            perf = pd.concat([perf, tmpDF])
    # clean up the indexing for the pandas dataframe
    perf = perf.reset_index(drop=True)
    return perf


def eval_opt(dtrain, dtest, yTest):
    param = {'max_depth': 9,
            'eta': 0.5,
            'objective':'binary:logistic'}
    bst = xgb.train(param, dtrain, 12)
    ypred = bst.predict(data=dtest)
    predictions = [round(value) for value in ypred]
    # evaluate predictions
    print(1-skm.accuracy_score(yTest, predictions))


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

    dtrain = xgb.DMatrix(xTrain, label=yTrain)
    dtest = xgb.DMatrix(xTest)

    res = search_params(dtrain)
    idx = res.groupby(['lr', 'md'])['test-error-mean'].idxmin()
    bestPerf = res.loc[idx]
    # sort best performance by test-error-mean
    print(bestPerf.sort_values(by='test-error-mean'))
    # get it as a label
    print(bestPerf.sort_values(by='test-error-mean').to_latex(index=False))
    eval_opt(dtrain, dtest, yTest)
