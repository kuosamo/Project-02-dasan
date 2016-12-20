# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import LabelEncoder
from konlpy.tag import Twitter
from konlpy.utils import pprint
import pandas as pd
import numpy as np

# 데이터 읽기
call = pd.read_csv('./Resource/dataset.csv')

y = call['디렉토리'] # target
X = call['질문']    # feature

# 클래수변수 encoder
le = LabelEncoder()
le.fit(y)
y = le.transform(y)

# train, test set
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    train_size=5387,
                                                    test_size=1347)

# machine_learn
class Machine(object):
    def __init__(self):
        pass

    # stop_word 함수
    def get_stop_words(self):
        result = set()
        for line in open('./Resource/stopwords-kr.txt', 'r').readlines():
            result.add(line.strip())
        return result

    # tokenize 함수
    def tokenize_pos(self, doc):
        pos_tagger = Twitter()
        return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]

    # modeling
    def training(self):
        # TfidfVectorizer((tokenizer, stop_words), SVC(kernel='linear'))
        clf_8 = Pipeline([('vect',
                            TfidfVectorizer(tokenizer=self.tokenize_pos,
                                            stop_words=self.get_stop_words())),
                           ('clf', SVC(kernel='linear'))])

        clf_8.fit(X_train, y_train)
        return clf_8

    # model score
    def test_score(self, clf_8):
        print (classification_report(y_test, clf_8.predict(X_test)))
        print (accuracy_score(y_test, clf_8.predict(X_test)))
