import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sgdLR
from lr import LinearRegression, file_to_numpy

xTrain = file_to_numpy('new_xTrain.csv')
yTrain = file_to_numpy('eng_yTrain.csv')
xTest = file_to_numpy('new_xTest.csv')
yTest = file_to_numpy('eng_yTest.csv')

# Subsample
randIndex = np.random.randint(len(xTrain), size=round(len(xTrain)*0.4))
xTrain_subset = xTrain[randIndex, :]
yTrain_subset = yTrain[randIndex]

result = []
epoch_range = range(1, 30)

lr = [0.00001, 0.0005, 0.001, 0.01, 0.1, 1]

for i in range(len(lr)):
		result.append([])
		model = sgdLR.SgdLR(lr[i], 1, 30)
		trainStats = model.train_predict(xTrain_subset, yTrain_subset, xTest, yTest)
		for epoch in epoch_range:
			result[i].append(trainStats[len(xTrain_subset)*epoch-1]['train-mse'])
		print(i)
fig = plt.figure()

plt.plot(range(1,30), result[0], 'b-', label='lr=0.00001')
plt.plot(range(1,30), result[1], 'r-', label='lr=0.0005')
plt.plot(range(1,30), result[2], 'g-', label='lr=0.001')
plt.plot(range(1,30), result[3], 'm-', label='lr=0.01')
plt.plot(range(1,30), result[4], 'y-', label='lr=0.1')
plt.plot(range(1,30), result[5], 'c-', label='lr=1')

plt.legend(loc='upper right', fontsize='medium')
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.title('SGD with Different Learning Rates')

fig.savefig('q3b.png', dpi = 300)
fig.show()