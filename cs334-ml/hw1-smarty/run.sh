#!/usr/bin/env bash

conda create -f environment.yml

k=5
XTRAIN="q3xTrain.csv"
YTRAIN="q3yTrain.csv"
XTEST="q3xTest.csv"
YTEST="q3yTest.csv"

python q1.py
python q2.py
python knn.py --xTrain $XTRAIN --yTrain $YTRAIN --xTest $XTEST --yTest $YTEST $k
python q4.py --xTrain $XTRAIN --yTrain $YTRAIN --xTest $XTEST --yTest $YTEST $k
python knn_graphs.py

conda env remove -n temp-env-smarty