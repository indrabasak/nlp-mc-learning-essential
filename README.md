# NLP with Python for Machine Learning Essential Training

This project contains examples from the LinkedIn course titled **NLP with Python for Machine Learning Essential Training**
by Derek Jedamski.

## How to install NLTK (Natural Language Toolkit) in Mac?
It assumes you already have Python installed. These instructions are
taken directly from [http://www.nltk.org/install.html](http://www.nltk.org/install.html).

### Install NLTK
From the terminal:

```
sudo pip3 install -U nltk
```
### Install Panda
From the terminal,

```
sudo pip3 install pandas
```

## Contents Examples

# 1. NLP Basics

### 1.1 What are NLP and NLTK?
Natural language processing is a field concerned with the ability of a computer to understand, analyze, manipulate, 
and potentially generate human language. 

By human language, we're simply referring to any language used for everyday communication. This can be English, 
Spanish, French, anything like that. Python doesn't naturally know what any given word means. All it sees is a 
string of characters.

The natural language toolkit is the most utilized package for handling natural language processing tasks in Python. 
Usually called NLTK for short, it is a suite of open-source tools originally created in 2001 at the University of 
Pennsylvania for the purpose of making building NLP processes in Python easier. This package has been expanded 
through the extensive contributions of open-source users in the years since its original development.

### [1.2 NLP Basics: What is Natural Language Processing & the Natural Language Toolkit?](./ch01/01_02.py)

### [1.3 NLP Basics: Reading in text data & why do we need to clean the text?](./ch01/01_03.py)

### [1.4 NLP Basics: Exploring the dataset](./ch01/01_04.py)

### [1.6 NLP Basics: NLP Basics: Learning how to use regular expressions](./ch01/01_06.py)

**Takeaways**

  - Useful methods for tokenizing
    - `findall()` - will search for the actual words while ignoring the things
    - `split()` will search for the characters that split the words while ignoring the actual words themselves
      
  - Useful regexes for tokenizing
    - `\W` & `\w` - words
    - `\S` & `\s` - whitespaces
