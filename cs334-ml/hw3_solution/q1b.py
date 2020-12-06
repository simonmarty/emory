import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn.linear_model as sklm

import selFeat

df = pd.read_csv("eng_xTrain.csv")
# do the feature extraction
df = selFeat.extract_features(df)
# merge xfeat with y
y = pd.read_csv('eng_yTrain.csv')
df['y'] = y

# calculate the correlation and perform the heatmap
corrMat = df.corr()
snsPlot = sns.heatmap(corrMat)
snsPlot.figure.savefig('corr_heatmap.eps', format='eps')
