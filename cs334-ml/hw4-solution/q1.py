import argparse
import numpy as np
import pandas as pd
from collections import Counter
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import GridSearchCV, StratifiedKFold, train_test_split

def model_assessment(filename):
    """
    Given the entire data, decide how
    you want to assess your different models
    to compare perceptron, logistic regression,
    and naive bayes, the different parameters, 
    and the different datasets.
    """
    Y = []
    X = []
    with open(filename) as fp:
       line = fp.readline()
       while line:
           label = [int(i) for i in line.split() if i.isdigit()]
           text = [i for i in line.split() if i.isdigit()==False]
           Y.append(label)
           X.append(text)
           line = fp.readline()
    data = {'y':np.ravel(Y), 'text':X}       
    df = pd.DataFrame(data)
    msk = np.random.rand(len(df)) < 0.7
    train = df[msk]
    test = df[~msk]
    return train, test


def build_vocab_map(train_set):
    word_counter = Counter()
    for s in range(train_set.shape[0]):
        word_counter.update(set(train.text.iloc[s]))
    fre_words = [k for k, v in word_counter.items() if v >= 30]
    return word_counter, fre_words


def construct_binary(train, frequent_words):
    """
    Construct the email datasets based on
    the binary representation of the email.
    For each e-mail, transform it into a
    feature vector where the ith entry,
    $x_i$, is 1 if the ith word in the 
    vocabulary occurs in the email,
    or 0 otherwise
    """
    binary_train = np.zeros((len(train), len(frequent_words)))
    for i in range(len(train)):
        words = set(train.text.iloc[i])
        for j in range(len(frequent_words)):
            if frequent_words[j] in words: 
                binary_train[i, j] = 1
    return binary_train 


def construct_count(train,frequent_words):
    """
    Construct the email datasets based on
    the count representation of the email.
    For each e-mail, transform it into a
    feature vector where the ith entry,
    $x_i$, is the number of times the ith word in the 
    vocabulary occurs in the email,
    or 0 otherwise
    """
    count_train = np.zeros((len(train), len(frequent_words)))
    for i in range(len(train)):
        words = list(train.text.iloc[i])
        for j in range(len(frequent_words)):
                count_train[i, j] = words.count(frequent_words[j])
    return count_train


def construct_tfidf(train, test, frequent_words):
    """
    Construct the email datasets based on
    the TF-IDF representation of the email.
    """
    train_corpus = []
    for i in range(len(train)):
        set1 = set(train.text.iloc[i])
        set2 = list(set1.intersection(frequent_words))
        my_lst_str =' '.join(map(str, set2))
        train_corpus.append(my_lst_str)
    test_corpus = []
    for i in range(len(test)):
        set1 = set(test.text.iloc[i])
        set2 = list(set1.intersection(frequent_words))
        my_lst_str =' '.join(map(str, set2))
        test_corpus.append(my_lst_str)
    TfidfVect = TfidfVectorizer(vocabulary=frequent_words)
    TfidfVect.fit(train_corpus)
    tf_train = TfidfVect.transform(train_corpus)
    tf_test = TfidfVect.transform(test_corpus)
    return tf_train.toarray(), tf_test.toarray()


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line


def NB_gauss(train, y, test, Y):
    clf = GaussianNB()
    clf.fit(train, y)
    y_hat = clf.predict(test)
    count =0
    for i in range(len(y_hat)):
        if(y_hat[i] != Y[i]):
            count +=1
    return count   

def Ber_gauss(train, y, test, Y):
    clf = BernoulliNB()
    clf.fit(train, y)
    y_hat = clf.predict(test)
    count =0
    for i in range(len(y_hat)):
        if(y_hat[i] != Y[i]):
            count +=1
    return count     

def multi_gauss(train, y, test, Y):
    clf = MultinomialNB()
    clf.fit(train, y)
    y_hat = clf.predict(test)
    count =0
    for i in range(len(y_hat)):
        if(y_hat[i] != Y[i]):
            count +=1
    return count     

def logistic(train, y, test, Y):
    clf = LogisticRegressionCV(cv=5, random_state=0).fit(train, y)
    y_hat = clf.predict(test)
    count =0
    for i in range(len(y_hat)):
        if(y_hat[i] != Y[i]):
            count +=1
    return count     


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data",
                        default="spamAssassin.data",
                        help="filename of the input data")
    args = parser.parse_args()
    train, test = model_assessment(args.data)
    word_map, frequent_words = build_vocab_map(train)
    frequent_words.sort()
    binary_train = construct_binary(train, frequent_words)
    binary_test = construct_binary(test, frequent_words)
    count_train = construct_count(train, frequent_words)
    count_test = construct_count(test, frequent_words)
    tfidf_train, tfidf_test = construct_tfidf(train, test, frequent_words)
    
    """Binary"""
    GaussNB_BinaryMistake = NB_gauss(binary_train, train.y.values, 
                               binary_test, test.y.values) 
    BerNB_BinaryMistake = Ber_gauss(binary_train, train.y.values, 
                           binary_test, test.y.values) 
    MultiNB_BinaryMistake = multi_gauss(binary_train, train.y.values, 
                           binary_test, test.y.values) 
    Logi_BinaryMistake = logistic(binary_train, train.y.values, 
                           binary_test, test.y.values)  
    
    """Count"""
    GaussNB_CountMistake = NB_gauss(count_train, train.y.values, 
                               count_test, test.y.values) 
    BerNB_CountMistake = Ber_gauss(count_train, train.y.values, 
                           count_test, test.y.values) 
    MultiNB_CountMistake = multi_gauss(count_train, train.y.values, 
                           count_test, test.y.values) 
    Logi_CountMistake = logistic(count_train, train.y.values, 
                           count_test, test.y.values)  
    
    """TFDIF dataset"""
    GaussNB_TfMistake = NB_gauss(tfidf_train, train.y.values, 
                           tfidf_test, test.y.values) 
    BerNB_TfMistake = Ber_gauss(tfidf_train, train.y.values,
                           tfidf_test, test.y.values) 
    MultiNB_TfMistake = multi_gauss(tfidf_train, train.y.values, 
                           tfidf_test, test.y.values) 
    Logi_TfMistake = logistic(tfidf_train, train.y.values, 
                           tfidf_test, test.y.values)  