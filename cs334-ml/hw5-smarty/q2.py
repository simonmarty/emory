import matplotlib.pyplot as plt
from rf import RandomForest, file_to_numpy


xTrain = file_to_numpy("q4xTrain.csv")
yTrain = file_to_numpy("q4yTrain.csv")
xTest = file_to_numpy("q4xTest.csv")
yTest = file_to_numpy("q4yTest.csv")


nests = range(1, 100)
results = []
for nest in nests:
    rf = RandomForest(nest=nest)
    res = rf.train(xTrain, yTrain)
    results.append(res[-1])

plt.xlabel("number of trees used")
plt.ylabel("OOB Error")
plt.plot(nests, results)
plt.savefig("nestcount")
plt.close()


rf = RandomForest(nest = 300)
res = rf.train(xTrain, yTrain)

plt.plot(range(300), res)
plt.save("progress")
plt.close()

maxFeats = range(1, xTrain.shape[1])
results = []
for featset_length in maxFeats:
    rf = RandomForest(maxFeat=featset_length)
    res = rf.train(xTrain, yTrain)
    results.append(res[-1])
plt.plot(maxFeats, results)
plt.xlabel("Number of features used")
plt.ylabel("OOB error")
plt.savefig("featamount")
plt.close()
