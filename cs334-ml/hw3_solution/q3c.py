import sgdLR
from lr import LinearRegression, file_to_numpy
import matplotlib.pyplot as plt



xTrain = file_to_numpy('new_xTrain.csv')
yTrain = file_to_numpy('eng_yTrain.csv')
xTest = file_to_numpy('new_xTest.csv')
yTest = file_to_numpy('eng_yTest.csv')

model = sgdLR.SgdLR(0.001, 1, 30)
trainStats = model.train_predict(xTrain, yTrain, xTest, yTest)
train_mse = []
test_mse = []
for i in range(1,30):
    train_mse_epoch = trainStats[len(xTrain)*i-1]['train-mse']
    train_mse.append(train_mse_epoch)

    test_mse_epoch = trainStats[len(xTrain)*i-1]['test-mse']
    test_mse.append(test_mse_epoch)

fig = plt.figure()
plt.plot(range(1,30), train_mse, 'b-', label='Training mse')
plt.plot(range(1,30), test_mse, 'r-', label='Test mse')

plt.legend(loc='upper right', fontsize='medium')
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.title('SGD with Optimal Learning Rate 0.001')

fig.savefig('q3c.png', dpi = 300)
fig.show()

