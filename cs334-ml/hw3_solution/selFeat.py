import argparse
import numpy as np
import pandas as pd
from sklearn import preprocessing


def is_morning(row):
    # calculate morning or not
    if row['hour'] > 5 and row['hour'] <= 12:
        return 1
    return 0

def is_afternoon(row):
    # calculate afternoon or not
    if row['hour'] > 12 and row['hour'] <= 18:
        return 1
    return 0  


def is_sleep(row):
    # calculate afternoon or not
    if row['hour'] > 22 or row['hour'] <= 5:
        return 1
    return 0  


def extract_features(df):
    # convert it to date
    df['date'] = pd.to_datetime(df['date'])
    # create an hour feature
    df['hour'] = df.date.dt.hour
    df['morning'] = df.apply(lambda row: is_morning(row), axis=1)
    df['afternoon'] = df.apply(lambda row: is_afternoon(row), axis=1)
    df['sleep'] = df.apply(lambda row: is_sleep(row), axis=1)
    # extract day of the week
    df['dow'] = df.date.dt.dayofweek
    df = df.drop(columns=['date'])
    return df


def select_features(df):
    """
    Select the features to keep
    """
    df.drop(columns=["T1", "RH_1", "RH_2",
                     "T3", "RH_3", "T4",
                     "RH_4", "T5", "RH_5",
                     "RH_6", "T7", "RH_7", "RH_9",
                     "T9", "T_out", "Press_mm_hg",
                     "Windspeed", "Visibility", "Tdewpoint",
                     "dow", "morning"],
            inplace=True)
    return df


def preprocess_data(trainDF, testDF):
    # standardize the two
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(trainDF)
    trainTr = pd.DataFrame(scaler.transform(trainDF),
                           columns=trainDF.columns)
    testTr = pd.DataFrame(scaler.transform(testDF),
                           columns=testDF.columns)
    return trainTr, testTr


def main():
    """
    Main file to run from the command line.
    """
    # set up the program to take in arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("outTrain",
                        help="filename of the updated training data")
    parser.add_argument("outTest",
                        help="filename of the updated test data")
    parser.add_argument("--trainFile",
                        default="eng_xTrain.csv",
                        help="filename of the training data")
    parser.add_argument("--testFile",
                        default="eng_xTest.csv",
                        help="filename of the test data")
    args = parser.parse_args()
    # load the train and test data
    xTrain = pd.read_csv(args.trainFile)
    xTest = pd.read_csv(args.testFile)
    # extract the new features
    xNewTrain = extract_features(xTrain)
    xNewTest = extract_features(xTest)
    # select the features
    xNewTrain = select_features(xNewTrain)
    xNewTest = select_features(xNewTest)
    # preprocess the data
    xTrainTr, xTestTr = preprocess_data(xNewTrain, xNewTest)
    # save it to csv
    xTrainTr.to_csv(args.outTrain, index=False)
    xTestTr.to_csv(args.outTest, index=False)


if __name__ == "__main__":
    main()



