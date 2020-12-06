import sgdLR
import lr
import matplotlib.pyplot as plt




xTrain = lr.file_to_numpy('new_xTrain.csv')
yTrain = lr.file_to_numpy('eng_yTrain.csv')
xTest = lr.file_to_numpy('new_xTest.csv')
yTest = lr.file_to_numpy('eng_yTest.csv')

batch_size = [1, 86, 215, 5590, 16770]
learning_rate = [1, 0.1, 0.001, 0.0005]
for j in range(1,len(batch_size)):
    result_mse = []
    epoch_range = range(1, 30)
    for i in range(len(learning_rate)):
        result_mse.append([])
        model = sgdLR.SgdLR(learning_rate[i], batch_size[j], 30)
        trainStats = model.train_predict(xTrain, yTrain, xTest, yTest)
        for epoch in epoch_range:
            result_mse[i].append(trainStats[len(xTrain) / batch_size[j] * epoch - 1]['train-mse'])

    fig = plt.figure()

    plt.plot(range(1, 30), result_mse[0], 'b-', label='lr=1')
    plt.plot(range(1, 30), result_mse[1], 'r-', label='lr=0.1')
    plt.plot(range(1, 30), result_mse[2], 'g-', label='lr=0.001')
    plt.plot(range(1, 30), result_mse[3], 'm-', label='lr=0.0005')

    plt.legend(loc='upper right', fontsize='medium')
    plt.xlabel('Epoch')
    plt.ylabel('MSE')
    plt.title('SGD with Different Learning Rates')

    fig.savefig('%d.png' %batch_size[j], dpi = 300)
    fig.show()













