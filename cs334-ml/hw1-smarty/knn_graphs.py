import q4
import knn
import pandas as pd
from numpy import mean
import matplotlib.pyplot as plt


def knn_variations(k, xTrain, yTrain, xTest, yTest):
    # no preprocessing
    acc1 = mean([q4.knn_train_test(k, xTrain, yTrain, xTest, yTest) for _ in range(5)])
    # preprocess the data using standardization scaling
    xTrainStd, xTestStd = q4.standard_scale(xTrain, xTest)
    acc2 = mean([q4.knn_train_test(k, xTrainStd, yTrain, xTestStd, yTest) for _ in range(5)])
    # preprocess the data using min max scaling
    xTrainMM, xTestMM = q4.minmax_range(xTrain, xTest)
    acc3 = mean([q4.knn_train_test(k, xTrainMM, yTrain, xTestMM, yTest) for _ in range(5)])
    # add irrelevant features
    xTrainIrr, yTrainIrr = q4.add_irr_feature(xTrain, xTest)
    acc4 = mean([q4.knn_train_test(k, xTrainIrr, yTrain, yTrainIrr, yTest) for _ in range(5)])

    return acc1, acc2, acc3, acc4


def knn_get_both_accuracies(k, xTrain, yTrain, xTest, yTest):
    model = knn.Knn(int(k))
    model.train(xTrain, yTrain['label'])
    # predict the training dataset
    yHatTrain = model.predict(xTrain)
    trainAcc = knn.accuracy(yHatTrain, yTrain['label'])
    # predict the test dataset
    yHatTest = model.predict(xTest)
    testAcc = knn.accuracy(yHatTest, yTest['label'])
    return trainAcc, testAcc


def plot_accuracy_graphs(xTrain, yTrain, xTest, yTest):
    df = pd.DataFrame(range(1, 50), columns=['k'])

    df[['no-preprocessing', 'standard-scale', 'min-max', 'irrelevant-feature']] = df.apply(
        lambda row: knn_variations(row['k'], xTrain, yTrain, xTest, yTest), axis=1, result_type='expand')
    df.plot(x='k', y=['no-preprocessing', 'standard-scale', 'min-max', 'irrelevant-feature'])
    # plt.gca().set_xticks(df["k"].unique())
    plt.title('KNN Accuracy over k')
    plt.ylabel('Accuracy')
    plt.savefig('accuracy-compare.png')
    plt.close()

    df[['train', 'test']] = df.apply(lambda row: knn_get_both_accuracies(row['k'], xTrain, yTrain, xTest, yTest),
                                     axis=1,
                                     result_type='expand')
    df.plot(x='k', y=['train', 'test'])
    plt.title('KNN Accuracy over k')
    plt.ylabel('Accuracy')
    plt.savefig('accuracy.png')
    plt.close()


if __name__ == '__main__':
    xTrain = pd.read_csv('q4xTrain.csv')
    yTrain = pd.read_csv('q4yTrain.csv')
    xTest = pd.read_csv('q4xTest.csv')
    yTest = pd.read_csv('q4yTest.csv')

    plot_accuracy_graphs(xTrain, yTrain, xTest, yTest)
