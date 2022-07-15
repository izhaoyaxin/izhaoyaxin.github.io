import math
import nltk
import math
import string

from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import*

from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer,TfidfTransformer
import preprocess
import input
import os,re
import numpy as np
from itertools import chain

#nltk.download('punkt')
#nltk.download('stopwords')

documents = input.file2text(file="context.txt")

#vectorizer = TfidfVectorizer(use_idf=True,max_df=0.5,min_df=1,ngram_range=(1,3))

#vectors = vectorizer.fit_transform(texts)
#print(vectorizer.get_feature_names())

###########
# keyword #
###########

def tf(word, count):
    return count[word] / sum(count.values())

def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)

def idf(word, count_list):
    return math.log(len(count_list)) / (1+n_containing(word, count_list))

def tf_idf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)

def count_word_term(document):
    tokens = preprocess.get_tokens(document)
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    stemmer = PorterStemmer()

    stemmed = preprocess.stem_tokens(filtered, stemmer)
    count = Counter(stemmed)
    return count


def keyword(doucments):
    countlist = []
    for doc in documents:
        countlist.append(count_word_term(doc))
        for i, count in enumerate(countlist):
            print("top words in document {}".format(i+1))
            scores = {word: tf_idf(word, count, countlist) for word in count}
            sorted_words = sorted(scores.items(), key = lambda x: x[1], reverse=True)
            for word, score in sorted_words[:5]:
                print("\tWords:{}, TF-IDF:{}".format(word, round(score, 5)))

#############
# keyphrase #
#############

def tf_idf_ngram(documents):
    """
    :param documents: type:list content: a set of documents
    """
    vocab = set(chain.from_iterable([doc.split() for doc in documents]))

    vectorizer = TfidfVectorizer(vocabulary=vocab)
    D =  vectorizer.fit_transform(documents)
    voc = dict((i, w) for w, i in vectorizer.vocabulary_.items())
    features = {}
    for i in range(D.shape[0]):
        Di =D.getrow(i)
        features[i] = list(zip([voc[j] for j in Di.indices], Di.data))

    return features

def get_ngram_keywords(docs_tokenzied,topk=5,num=2):
    docs_ngrams = [preprocess.gene_ngram(doc,max_num=num,min_num=num) for doc in docs_tokenzied]
    docs_ngrams = [preprocess.clean_ngrams(doc) for doc in docs_ngrams]

    docs_ = []
    for doc in docs_ngrams:
        docs_.append(' '.join(['_'.join(ngram) for ngram in doc]))
        features = tf_idf_ngram(docs_)
    docs_keys = []
    for i,pair in features.items():
        topk_idx = np.argsort([v for w,v in pair])[::-1][:topk]
        docs_keys.append([pair[idx][0] for idx in topk_idx])

    return [[' '.join(words.split('_')) for words in doc ] for doc in docs_keys]

def keyphrase(documents,topk):
    lemmatizer = nltk.WordNetLemmatizer()
    docs_tokenized = preprocess.tokenize_doc(documents)
    ngrams = preprocess.gene_ngram(docs_tokenized)

    docs_tokenized = [list(chain.from_iterable(doc)) for doc in docs_tokenized]
    docs_keys = []
    for n in [1,2,3]:
        #if n == 1:
        #    docs_tokenized = [[lemmatizer.lemmatize(word) for word in doc] for doc in docs_tokenized]
        keys_ngram = get_ngram_keywords(docs_tokenized,topk,num=n)
        docs_keys.append(keys_ngram)

    return [uni+bi+tri for uni,bi,tri in zip(*docs_keys)]


if __name__ == '__main__':
    #keyword(documents)
    #print(documents)
    print(keyphrase(documents,10))
