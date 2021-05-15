# NLP Basics: Learning how to use regular expressions

# Using regular expressions in Python
# Python's re-package is the most commonly used regex resource.
# More details can be found [here](https://docs.python.org/3/library/re.html.

import re

re_test = 'This is a made up string to test 2 different regex methods'
print(re_test + '\n')

re_test_messy = 'This      is a made up     string to test 2    different regex methods'
print(re_test_messy + '\n')


re_test_messy1 = 'This-is-a-made/up.string*to>>>>test----2""""""different~regex-methods'
print(re_test_messy1 + '\n')

# Splitting a sentence into a list of words

# split a sentence using regex for a single white space separating words
words = re.split('\s', re_test)
print(words)
print('\n')

# split a sentence using regex for multiple white spaces separating words
words = re.split('\s+', re_test_messy)
print(words)
print('\n')

# split a sentence using regex with one or more of any non-word character
words = re.split('\W+', re_test_messy1)
print(words)
print('\n')

# instead of splitting a sentence based on regex, find words which matches continuous non-whitespace characters
words = re.findall('\S+', re_test)
print(words)
print('\n')

# instead of splitting a sentence based on regex, find words which matches continuous non-whitespace characters
# separating them
words = re.findall('\S+', re_test_messy)
print(words)
print('\n')

# instead of splitting a sentence based on regex, find words which matches continuous word characters
# separating them
words = re.findall('\w+', re_test_messy1)
print(words)
print('\n')