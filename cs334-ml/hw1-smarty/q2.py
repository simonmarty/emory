# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING CODE
# WRITTEN BY OTHER STUDENTS.
# Simon Marty

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris

if __name__ == '__main__':
    iris = load_iris()

    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                      columns=iris['feature_names'] + ['species'])

    df.replace({'species': {
        0.0: 'setosa',
        1.0: 'versicolor',
        2.0: 'virginica'
    }}, inplace=True)

    for i, attribute in enumerate(list(df.columns)[:-1]):
        df.boxplot(column=attribute, by='species')
        plt.xlabel('Species')
        plt.ylabel(attribute)
        plt.title(f'{attribute[:-5]} per species')
        plt.suptitle('')
        plt.savefig(f'box{i}.png')
        plt.close()

    sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue=df.species.tolist(), data=df)
    plt.savefig('scatter1.png')
    plt.close()

    sns.scatterplot(x='petal length (cm)', y='petal width (cm)', hue=df.species.tolist(), data=df)
    plt.savefig('scatter2.png')
    plt.close()
