# NLP Basics: What is Natural Language Processing & the Natural Language Toolkit?

# Download NLTK data
import nltk

dir(nltk)

# What can you do with NLTK?
from nltk.corpus import stopwords

print(stopwords.words('english')[0:500:25])