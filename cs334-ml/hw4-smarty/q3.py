import pandas as pd
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    datasets = {
        "binary": [pd.read_csv("X_train_binary.csv"), pd.read_csv("X_test_binary.csv")],
        "count": [pd.read_csv("X_train_count.csv"), pd.read_csv("X_test_count.csv")],
    }

    y_train = pd.read_csv("y_train.csv")['labels']
    y_test = pd.read_csv("y_test.csv")['labels']

    for dname, dataset in datasets.items():
        methods = {
            'bernoulli': BernoulliNB(),
            'multinomial': MultinomialNB(),
            'logistic': LogisticRegression(),
        }
        for name, m in methods.items():
            m.fit(dataset[0], y_train)
            print({
                "method": name,
                "dataset": dname,
                "accuracy": m.score(dataset[1], y_test)
            })
