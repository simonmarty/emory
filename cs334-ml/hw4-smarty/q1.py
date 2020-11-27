import argparse
import numpy as np
from typing import Dict
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

from sklearn.preprocessing import MinMaxScaler


def model_assessment(filename):
    """
    Given the entire data, decide how
    you want to assess your different models
    to compare perceptron, logistic regression,
    and naive bayes, the different parameters, 
    and the different datasets.
    """

    d = {'labels': [], 'words': [], 'lines': []}
    with open(filename) as file:
        for line in file:
            tokens = line.split(" ")
            d['labels'].append(int(tokens[0]))
            d['lines'].append(line[1:].strip())
            d['words'].append(np.array(tokens[1:]))

    df = pd.DataFrame(d)

    return train_test_split(df[['words', 'lines']], df['labels'], test_size=0.3)


def build_vocab_map(df: pd.DataFrame) -> Dict:
    return {
        k: v for k, v in
        Counter([
            word for sentence in df['words']
            for word in set(sentence)
        ]).items()
        if v >= 30
    }


def construct_binary(df, vocab):
    """
    Construct the email datasets based on
    the binary representation of the email.
    For each e-mail, transform it into a
    feature vector where the ith entry,
    $x_i$, is 1 if the ith word in the 
    vocabulary occurs in the email,
    or 0 otherwise
    """
    cv = CountVectorizer(vocabulary=vocab, binary=True)
    matrix = cv.fit_transform(df['lines'])

    return pd.DataFrame(MinMaxScaler().fit_transform(pd.DataFrame(matrix.toarray())), columns=vocab)


def construct_count(df, vocab):
    """
    Construct the email datasets based on
    the count representation of the email.
    For each e-mail, transform it into a
    feature vector where the ith entry,
    $x_i$, is the number of times the ith word in the 
    vocabulary occurs in the email,
    or 0 otherwise
    """
    cv = CountVectorizer(vocabulary=vocab)
    matrix = cv.fit_transform(df['lines'])

    return pd.DataFrame(MinMaxScaler().fit_transform(pd.DataFrame(matrix.toarray())))


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--data",
                        default="spamAssassin.data",
                        help="filename of the input data")
    args = parser.parse_args()

    X_train, X_test, y_train, y_test = model_assessment(args.data)

    for k, v in {'y_train': y_train, 'y_test': y_test}.items():
        v.to_csv(f'{k}.csv')

    vocab = build_vocab_map(X_train)

    for k, v in {'X_train': X_train, 'X_test': X_test}.items():
        construct_binary(v, vocab.keys()).to_csv(f"{k}_binary.csv", index=False)
        construct_count(v, vocab.keys()).to_csv(f"{k}_count.csv", index=False)


if __name__ == "__main__":
    main()
