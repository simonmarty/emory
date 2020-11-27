import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse
from dt import dt_train_test, DecisionTree


if __name__ == "__main__":
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
    # create an instance of the decision tree using gini

    
    maxDepth = np.arange(1,10)
    minLeaf = np.arange(1,10)
    trainauc = np.ones((9,9))
    testauc = np.ones((9,9))
    X, Y = np.meshgrid(maxDepth, minLeaf)
        
    for m in maxDepth:
        for l in minLeaf:
            dt = DecisionTree('gini', m, l)
            trainauc[m-1,l-1], testauc[m-1, l-1] = dt_train_test(dt, xTrain, yTrain, xTest, yTest)
    fig = plt.figure(figsize=(9,5))
    ax = plt.axes(projection="3d")
    ax.plot_wireframe(X, Y, trainauc, color='g',label='Train')
    ax.plot_wireframe(X, Y, testauc, color='r',label='Test')
    ax.set_title('3D plot of accuracy using Gini')
    ax.set_xlabel('Min Leaf Samples')
    ax.set_ylabel('Tree Depth')
    ax.set_zlabel('Accuracy')
    ax.legend()
    plt.savefig('q1c.eps', format='eps', dpi=1000)
    plt.show()
    
    

