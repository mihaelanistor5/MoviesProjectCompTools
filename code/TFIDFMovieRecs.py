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
import pickle5 as pickle

def combine_document(df,movielist):
    DocumentDict = {}
    for movie in movielist:
        keywords = ''
        document = df[df['original_title'] == movie]['keywords']
        for ele in ast.literal_eval(document.values[0]):
            keywords += ele['name']+' '
        keywords += str(df[df['original_title'] == movie]['overview'])
        DocumentDict[movie] = keywords
    return DocumentDict

def train_model(Dict,nclusters,vectorizer):
    documents = DocumentDict.values()
    X = vectorizer.fit_transform(documents)
    return X

def score_movies(Dict,vectorizer):
    MovieDict = {}
    for movie in Dict:
        Y = vectorizer.transform([Dict[movie]])
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
    df1 = pd.read_csv('/Users/'+username+'/MoviesProjectCompTools/ratings_and_sentiment_v2.csv')
    directory = '/Users/'+username+'/MoviesProjectCompTools/dataset_5000/tmdb_5000_movies.csv'
    df = pd.read_csv(directory)
    # Find the common movies between the two conflicting datasets
    common = []    
    for movie in df['original_title']:
        if movie in df1['original_title'].tolist():
            common.append(movie)

    # Initialize the TFIDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    # Compile all the movie documents, i.e. keywords and movie descriptions
    DocumentDict = combine_document(df,common)
    # Once we have the list of movies and dataframes we compute the TFIDF scores of all the documents
    model = train_model(DocumentDict,10,vectorizer)
    # Create a dictionary that organizes movies with their TFIDF matrix
    MovieDict = score_movies(DocumentDict,vectorizer)
    # Finally given any movie in the dataset, the 5 movies with the most in common will be recommended
    recommend_movies(MovieDict,'Borat: Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan',5)
