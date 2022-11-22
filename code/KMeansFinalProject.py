import pandas as pd
import os
import pwd
import glob
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
import numpy as np
import ast

def combine_document(df):
    DocumentDict = {}
    movielist = df['original_title'].tolist()
    i=0
    for movie in movielist:
        keywords = ''
        document = df[df['original_title'] == movie]['keywords']
        for ele in ast.literal_eval(document.values[0]):
            keywords += ele['name']+' '
        keywords += str(df[df['original_title'] == movie]['overview'][i])
        DocumentDict[movie] = keywords
        i+=1
    return DocumentDict

def train_model(Dict,nclusters,vectorizer):
    documents = DocumentDict.values()
    X = vectorizer.fit_transform(documents)
#    model = KMeans(n_clusters=nclusters, init='k-means++', max_iter=100, n_init=1)
#    model.fit(X)
#    return model

def score_movies(Dict,vectorizer):
    MovieDict = {}
    for movie in Dict:
        Y = vectorizer.transform([Dict[movie]])
#        prediction = model.predict(Y)
        MovieDict[movie] = Y
    return MovieDict

def recommend_movies(Dict,movie1,n_recs):
    RecDict = {}
    for movie in Dict:
        dotprod = np.dot(Dict[movie1].toarray(),np.transpose(Dict[movie].toarray()))
        RecDict[movie] = dotprod
    recs = sorted(RecDict, key=RecDict.get, reverse=True)[1:n_recs+1]
    print('If you liked '+movie1+' you will also like:')
    print(recs)
    return RecDict

if __name__ == '__main__':
    username = pwd.getpwuid(os.getuid())[0]
    directory = '/Users/'+username+'/MoviesProjectCompTools/dataset_5000/tmdb_5000_movies.csv'
    ### ^THIS IS DIRECTORY FOR CSV FILE ON MY COMPUTER - COULDNT GET IT TO ACCESS STRAIGHT FROM GIT
    df = pd.read_csv(directory)
    #df = pd.read_csv('https://github.com/mihaelanistor5/MoviesProjectCompTools/blob/main/dataset_5000/tmdb_5000_movies.csv')

    vectorizer = TfidfVectorizer(stop_words='english')
    DocumentDict = combine_document(df)
    model = train_model(DocumentDict,10,vectorizer)
    MovieDict = score_movies(DocumentDict,vectorizer)
    recommend_movies(MovieDict,'Avatar',5)


