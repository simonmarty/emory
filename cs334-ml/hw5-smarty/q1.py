import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_curve

datasets = {}
datasets['x_train'] = pd.read_csv('q4xTrain.csv')
datasets['x_test'] = pd.read_csv('q4xTest.csv')
datasets['y_train'] = pd.read_csv('q4yTrain.csv')['label']
datasets['y_test'] = pd.read_csv('q4yTest.csv')['label']


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    scaler = MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(df))


datasets['x_train'] = normalize(datasets['x_train'])
datasets['x_test'] = normalize(datasets['x_test'])

logistic = LogisticRegression(penalty='none')
logistic.fit(datasets['x_train'], datasets['y_train'])
print(
    f"Logistic Regression Score on non-PCA data: {logistic.score(datasets['x_test'], datasets['y_test'])}")

pca = PCA(n_components=0.95)
pca.fit(datasets['x_train'], datasets['y_train'])

transformed_data = {}
transformed_data['x_train'] = pca.transform(datasets['x_train'])
transformed_data['x_test'] = pca.transform(datasets['x_test'])

logisticPCA = LogisticRegression(penalty='none')
logisticPCA.fit(transformed_data['x_train'], datasets['y_train'])
print(
    f"Logistic Regression Score on PCA data: {logisticPCA.score(transformed_data['x_test'], datasets['y_test'])}")

print(pd.DataFrame(pca.components_, columns=datasets['x_train'].columns))

falsepos, truepos, _ = roc_curve(
    datasets['y_test'], logistic.predict_proba(datasets['x_test'])[:, 1])
falseposPCA, trueposPCA, _ = roc_curve(
    datasets['y_test'], logisticPCA.predict_proba(transformed_data['x_test'])[:, 1])

plt.figure(figsize=(10, 6))
plt.plot(falsepos, truepos, label="Without PCA")
plt.plot(falseposPCA, trueposPCA, label="With PCA")
plt.legend()
plt.show()
