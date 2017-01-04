# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize

#Import custom stopwords from file
stopwords_file = open('stopwords.txt', 'r')
stopwords = [x for x in stopwords_file.read().split()]

def cleanText(text):

    #Tokenize string
    words = word_tokenize(text.lower())

    #Remove stopwords
    important_words = filter(lambda x: x not in stopwords, words)

    return important_words






