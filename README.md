# English or Arabic Article Search System 

Below is the list of implemented functionalities in this rank retrival model. which can be multiporposely used to search data from given corpus in both english in arabic.

## Functionality Implemented

  1. Searching top 10 article based on query given
  2. Comparing Similarity Between two Articles present in corpus
  3. Wilcard Query
  4. Term Auto-completion


# The Corpus 
 * [English Corpus](https://dumps.wikimedia.org/enwiki/latest/) - Articles were downloaded using the above.
 * [Arabic Corpus](https://dumps.wikimedia.org/arwiki/latest/) - Articles were downloaded using the above


## Software frameworks used:

 * [python-nltk](http://www.nltk.org/) - NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces
 
    *Install NLTK: run sudo pip install -U nltk
    *Install Numpy (optional): run sudo pip install -U numpy
    *Test installation: run python then type import nltk

 * [python-flask](https://www.loomio.org/) - frame work to creade a frontend interactive application in python. [Installing flask in python](http://hanzratech.in/2015/01/16/setting-up-flask-in-ubuntu-14-04-in-virtual-environment.html)
 
 * [WikiExtractor](https://github.com/attardi/wikiextractor) WikiExtractor.py is a Python script that extracts and cleans text from a Wikipedia database dump.

The tool is written in Python and requires Python 2.7 or Python 3.3+ but no additional library. 

 
## Platforms:

 * This can be used on any browser that support javascript,css and jquery provided we have server made.
 * To make server we need python with both python nltk and flask installed.
 
## Project Extention
 * Creating Query Logs and using machine learning technique to use logs to implement more efficient query searching in corpus.
