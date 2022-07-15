#coding:utf-8
import nltk
import math
import string

from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
import os,re
import numpy as np
from itertools import chain
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag,word_tokenize,sent_tokenize

###########
# keyword
###########

def get_tokens(document):
    lower = document.lower()
    remove_punctuation_map = dict((ord(char),None) for char in string.punctuation)
    no_punctuation = lower.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)

    return tokens

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))

    return stemmed

###########
#keyphrase
###########

def tokenize_doc(documents):
    docs_tokenized = []
    for doc in documents:
        doc = re.sub('[\n\r\t]+',' ',doc)

        # split sentence
        sents = sent_tokenize(doc)

        # split word
        sents_tokenized = [word_tokenize(sent.strip()) for sent in sents]
        docs_tokenized.append(sents_tokenized)

    return docs_tokenized

def gene_ngram(sentence,max_num=3,min_num=2):
    """
    :param sentence: split sentence
    :param max: max=3，3-gram
    :param min: min=1，keep 1-gram
    :return:
    """
    if len(sentence) < max_num:
        max = len(sentence)

    ngrams = [sentence[i-k:i] for k in range(min_num,max_num+1) for i in range(k, len(sentence)+1)]
    return ngrams

def clean_by_len(gram):

    for word in gram:
        if len(word)<2:
            return False
    return True

def clean_ngrams(ngrams):
    #stopwords = open("mystopwords.txt",encoding="utf-8").readlines()
    #stopwords = [word.strip() for word in stopwords]
    pat = re.compile("[0-9]+")

    #ngrams = [gram for gram in ngrams if len(set(stopwords).intersection(set(gram)))==0]
    #ngrams = [gram for gram in ngrams if len(pat.findall(''.join(gram).strip()))==0]
    #ngrams = [gram for gram in ngrams if clean_by_len(gram)]

    allow_pos_one = ["NN","NNS","NNP","NNPS"]
    allow_pos_two = ["NN","NNS","NNP","NNPS","JJ","JJR","JJS"]
    allow_pos_three = ["NN","NNS","NNP","NNPS","VB","VBD","VBG","VBN","VBP","VBZ","JJ","JJR","JJS"]

    ngrams_filter = []
    for gram in ngrams:
        words,pos = zip(*pos_tag(gram))

        if len(words) == 1:
            if not pos[0] in allow_pos_one:
                continue
            ngrams_filter.append(gram)

        else:
            if not (pos[0] in allow_pos_three and pos[-1] in allow_pos_one):
                continue
            ngrams_filter.append(gram)
    return ngrams_filter

