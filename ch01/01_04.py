# NLP Basics: Exploring the dataset

# Read in text data

import pandas as pd

# read the data set, use '\t` as delimiter, and there are no headers in the file
fullCorpus = pd.read_csv('../data/SMSSpamCollection.tsv', sep='\t', header=None)

# name the columns
fullCorpus.columns = ['label', 'body_text']

print(fullCorpus.head())
print('\n')

# Explore the dataset
# What is the shape of the dataset?
print("Input data has {} rows and {} columns".format(len(fullCorpus), len(fullCorpus.columns)))
print('\n')

# How many spam/ham are there?
print("Out of {} rows, {} are spam, {} are ham".format(len(fullCorpus),
                                                       len(fullCorpus[fullCorpus['label']=='spam']),
                                                       len(fullCorpus[fullCorpus['label']=='ham'])))
print('\n')

# How much missing data is there?

print("Number of null in label: {}".format(fullCorpus['label'].isnull().sum()))
print("Number of null in text: {}".format(fullCorpus['body_text'].isnull().sum()))