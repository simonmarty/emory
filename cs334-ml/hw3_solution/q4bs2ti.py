import sgdLR
from lr import LinearRegression, file_to_numpy
import standardLR
import matplotlib.pyplot as plt

# load the datasets
xTrain = file_to_numpy('new_xTrain.csv')
yTrain = file_to_numpy('eng_yTrain.csv')
xTest =  file_to_numpy('new_xTest.csv')
yTest =  file_to_numpy('eng_yTest.csv')

best_lr = [0.1,0.1,0.1,0.1,0.1]
batchsizes = [1, 86, 215, 5590, 16770]
colormap = ['blue', 'pink', 'orange', 'black','cyan']
# Closer Form
model_cf = standardLR.StandardLR()
trainStats_cf = model_cf.train_predict(xTrain, yTrain, xTest, yTest)
time_cf = trainStats_cf[0]['time']
mse_train_cf = trainStats_cf[0]['train-mse']
mse_test_cf = trainStats_cf[0]['test-mse']

fig_train = plt.figure()
axes_train = fig_train.add_subplot(1,1,1)
axes_train.plot(time_cf, mse_train_cf, 'r.', label='Closed Form Solution')

fig_test = plt.figure()
axes_test = fig_test.add_subplot(1,1,1)
axes_test.plot(time_cf, mse_test_cf, 'r.', label='Closed Form Solution')

for i in range(len(batchsizes)):
    model = sgdLR.SgdLR(best_lr[i], batchsizes, 10)
    trainStats = model.train_predict(xTrain, yTrain, xTest, yTest)
    time = []
    mse_train = []
    mse_test = []
    for j in trainStats:
        time.append(trainStats[j]['time'])
        mse_train.append(trainStats[j]['train-mse'])
        mse_test.append(trainStats[j]['test-mse'])
    axes_train.plot(time, mse_train, '.', color=colormap[i], label='bs=%d' % batchsizes[i])
    axes_test.plot(time, mse_train, '.', color=colormap[i], label='bs=%d' % batchsizes[i])


axes_train.legend(loc='upper right', fontsize='small')
axes_train.set_xlabel('Time(sec)')
axes_train.set_ylabel('MSE')
axes_train.set_title('Different Batch Sizes on Training set')
axes_train.set_xlim([0, 1])

fig_train.savefig('q4train.png',dpi =300)
fig_train.show()


axes_test.legend(loc='upper right', fontsize='small')
axes_test.set_xlabel('Time(sec)')
axes_test.set_ylabel('MSE')
axes_test.set_title('Different Batch Sizes on Training set')
axes_test.set_xlim([0, 1])

fig_test.savefig('q4test.png',dpi = 300)
fig_test.show()

