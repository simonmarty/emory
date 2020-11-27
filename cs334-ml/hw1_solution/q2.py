from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load the iris dataset using sklearn
iris = datasets.load_iris()

# we can set it into pandas since that's what we're using to plot
irisDF = pd.DataFrame(iris.data,
                     columns=['sepal_len', 'sepal_width',
                              'petal_len', 'petal_width'])
irisDF['target'] = iris.target

# pandas way to do boxplot the different ones and group by target
bpFig = irisDF.boxplot(column=['sepal_len', 'sepal_width',
                       'petal_len', 'petal_width'],
                       by=['target'])
plt.savefig('q2b-pd.png')

# pandas way to do scatter plot
sepalPlt = irisDF.plot.scatter(x='sepal_len',
                               y='sepal_width',
                               c='target',
                               colormap='viridis')
plt.savefig('q2c-sepal-pd.png')
sepalPlt = irisDF.plot.scatter(x='petal_len',
                               y='petal_width',
                               c='target',
                               colormap='viridis')
plt.savefig('q2c-petal-pd.png')

# seaborn way to do it -- first load the data
iris = sns.load_dataset("iris")
# do the boxplots for (b)
plt.clf()  # clear the figure
b1 = sns.boxplot(x="species", y="sepal_length",
                 data=iris)
b1.get_figure().savefig('q2b-sl-seaborn.png')
plt.clf()  # clear the figure
b2 = sns.boxplot(x="species", y="sepal_width",
                 data=iris)
b2.get_figure().savefig('q2b-sw-seaborn.png')
plt.clf() 
b3 = sns.boxplot(x="species", y="petal_length",
                 data=iris)
b3.get_figure().savefig('q2b-pl-seaborn.png')
plt.clf() 
b4 = sns.boxplot(x="species", y="petal_width",
                 data=iris)
b4.get_figure().savefig('q2b-pw-seaborn.png')

# do the scatter plots for (c)
sns.lmplot(x="sepal_length", y="sepal_width",
           data=iris, hue="species",
           fit_reg=False, legend=False)
plt.legend()
plt.savefig('q2c-sepal-sns.png')

sns.lmplot(x="petal_length", y="petal_width",
           data=iris, hue="species",
           fit_reg=False, legend=False)
plt.legend()
plt.savefig('q2c-petal-sns.png')

