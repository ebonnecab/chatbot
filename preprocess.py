#imports
import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle

'''
The first step is to import the JSON data file.
This file contains tags, patterns and responses.
The purpose of the various categories is to classify the user input
then output a random selection from the list of appropriate responses
'''

words = []
classes = []
ignore_words = ['?', '!']

def load_parse_file(data_file):
    with open(data_file) as f:
        intents = json.loads(f.read())
    return intents


if __name__ == '__main__':
    test = load_parse_file("intents.json")
    print(test)