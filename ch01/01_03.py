# NLP Basics: Reading in text data & why do we need to clean the text?

# Read in the raw text
rawData = open("../data/SMSSpamCollection.tsv").read()

# Print the raw data - first 500 characters
print(rawData[0:500])
print('\n')

# replace `\t` with `\n` and then split the data on `\n`
parsedData = rawData.replace('\t', '\n').split('\n')

print(parsedData[0:5])
print('\n')

# read data from index 0 and jump every other index
labelList = parsedData[0::2]
print(labelList[0:5])
print('\n')

# read data from index 1 and jump every other index
textList = parsedData[1::2]
print(textList[0:5])
print('\n')

print(labelList[-5:])

import pandas as pd

fullCorpus = pd.DataFrame({
    'label': labelList[0:-1],
    'body_list': textList
})

print(fullCorpus.head())

#faster way of parsing data
dataset = pd.read_csv("../data/SMSSpamCollection.tsv", sep="\t", header=None)
print(dataset.head())