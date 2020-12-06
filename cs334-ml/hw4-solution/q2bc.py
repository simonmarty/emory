from perceptron import Perceptron, calc_mistakes, file_to_numpy
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
# Read Binary datasets
xTrain_bin = file_to_numpy("BinaryXTrain.csv")
yTrain_bin = file_to_numpy("yTrain.csv")
xTest_bin = file_to_numpy("BinaryXTest.csv")
yTest_bin = file_to_numpy("yTest.csv")
# Read Count datasets
xTrain_co = file_to_numpy("CountXTrain.csv")
yTrain_co = file_to_numpy("yTrain.csv")
xTest_co = file_to_numpy("CountXTest.csv")
yTest_co = file_to_numpy("yTest.csv")

#Read Tfidf datasets
xTrain_tf = file_to_numpy("TfidfXTrain.csv")
yTrain_tf = file_to_numpy("yTrain.csv")
xTest_tf = file_to_numpy("TfidfXTest.csv")
yTest_tf = file_to_numpy("yTest.csv")

# #Parameter tuning
iterns = [1,30,50,100,500,1000]
def kfold_validation(xtrain, ytrain,foldnum,epochnum):
    kfold = KFold(n_splits=foldnum)
    mistake = []
    for epoch in epochnum:
        total = 0
        for trainIndex, testIndex in kfold.split(xtrain):
            xTrain_k, xTest_k = xtrain[trainIndex], xtrain[testIndex]
            yTrain_k, yTest_k = ytrain[trainIndex], ytrain[testIndex]
            model = Perceptron(epoch)
            trainStats = model.train(xTrain_k, yTrain_k)
            yHat = model.predict(xTest_k)
            total += calc_mistakes(yHat, yTest_k)
        average_mistakes = total / foldnum
        mistake.append(average_mistakes)
    return mistake
def obtain_words(model, xTrain)
    indices = np.argsort(model.w)
    xFeat = pd.read_csv(args.xTrain)
    words_list = list(xFeat.columns.values)
    indices_pos = indices[-15:]
    words_pos = []
    for i in reversed(range(15)):
        index = indices_pos[i]
        words_pos.append(words_list[index])
    # get 15 words with most negative weights
    indices_neg = indices[:15]
    words_neg = []
    for i in range(15):
        index = indices_neg[i]
        words_neg.append(words_list[index])
    return words_pos, words_neg
#Train new model based on the best parameters
#For Binary datasets
recval_bin = kfold_validation(xTrain_bin, yTrain_bin, 5, iterns)
perc1 = Perceptron(int(iterns[recval_bin.index(min(recval_bin))]))
perc1.train(xTrain_bin, yTrain_bin)
Error1 = calc_mistakes(perc1.predict(xTest_bin), yTest_bin)
pos1,neg1 = obtain_words(perc1, xTrain_bin)
print('Average mistake for each fold in Binary dataset', recval_bin)
print("The mistake before algorithm terminates is", perc1.error[-2])
print("The best optimal eopch number is", iterns[recval_bin.index(min(recval_bin))])
print("The error for Binary test dataset is", Error1)
print("Positive words are", pos1)
print("Negtive words are", neg1)

#For Count datasets
recval_co = kfold_validation(xTrain_co, yTrain_co, 5, iterns)
perc2 = Perceptron(int(iterns[recval_co.index(min(recval_co))]))
perc2.train(xTrain_co, yTrain_co)
Error2 = calc_mistakes(perc2.predict(xTest_co), yTest_co)
pos2,neg2 = obtain_words(perc2, xTrain_co)
print('Average mistake for each fold in Count dataset', recval_co)
print("The mistake before algorithm terminates is", perc2.error[-2])
print("The best optimal eopch number is", iterns[recval_co.index(min(recval_co))])
print("The error for Count test dataset is", Error2)
print("Positive words are", pos2)
print("Negtive words are", neg2)

#For Tf-idf datasets
recval_tf = kfold_validation(xTrain_tf, yTrain_tf, 5, iterns)
perc3 = Perceptron(int(iterns[recval_tf.index(min(recval_tf))]))
perc3.train(xTrain_tf, yTrain_tf)
Error3 = calc_mistakes(perc3.predict(xTest_tf), yTest_tf)
pos3,neg3 = obtain_words(perc3, xTrain_tf)
print('Average mistake for each fold in Tf-idf dataset', recval_tf)
print("The mistake before algorithm terminates is", perc3.error[-2])
print("The best optimal eopch number is", iterns[recval_tf.index(min(recval_tf))])
print("The error for Tf-idf test dataset is", Error3)
print("Positive words are", pos3)
print("Negtive words are", neg3)
