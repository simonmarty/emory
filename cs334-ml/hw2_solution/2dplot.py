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

	maxDepth = list(np.arange(1,10))
	minLeaf = list(np.arange(1,10))
	yDepth = np.ones((9,2))
	yLeaf = np.ones((9,2))

	for m in maxDepth:
		dt = DecisionTree('gini', m, 5)
		trainauc, testauc = dt_train_test(dt, xTrain, yTrain, xTest, yTest)
		yDepth[m-1,0] = trainauc
		yDepth[m-1,1] = testauc

	for l in minLeaf:
		dt = DecisionTree('gini', 5, l)
		trainauc, testauc = dt_train_test(dt, xTrain, yTrain, xTest, yTest)
		yLeaf[l-1,0] = trainauc
		yLeaf[l-1,1] = testauc


	plt.subplot(1,2,1)
	plt.plot(maxDepth, yDepth[:,0], color = 'g', label='Train')
	plt.plot(maxDepth, yDepth[:,1], color = 'r', label='Test')
	plt.xlabel('Tree Depth')
	plt.ylabel('Accuracy')
	plt.legend(loc="upper left")

	plt.subplot(1,2,2)
	plt.plot(minLeaf, yLeaf[:,0], color = 'g', label='Train')
	plt.plot(minLeaf, yLeaf[:,1], color = 'r', label='Test')
	plt.xlabel('Min Leaf Samples')

	plt.suptitle('2D plots of accuracy using gini')
	plt.savefig('q1c_2d.png', format='png', dpi=1000)
	plt.show()
	