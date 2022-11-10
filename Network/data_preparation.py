import pandas as pd
import os

# path to parent folder
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#%% OBJECTS AND FUNCTIONS

def fun(arg):
    pass

#%% PREPARE DATASET 
"""
    Create a dataframe of users and movies they reviewed
    
        (only for common movies in both datasets)
"""

# get list of a movies from 5000 file
movies_5000 = pd.read_csv(os.path.join(path, "dataset_5000", "tmdb_5000_movies.csv"),
                          usecols = ["original_title"])
movies_5000 = movies_5000.original_title.tolist()


#---------------------------------------------------------------------------------------------
# list of file paths to import
file_paths = []
for root, _, files in os.walk(os.path.join(path, "dataset_review\\2_reviews_per_movie_raw")):
    for filename in files:
        file_paths.append(os.path.join(root, filename))


#---------------------------------------------------------------------------------------------
# create dictionary with movie title and corresponding path
movies = dict()
for movie in file_paths:
    #title = os.path.basename(movie)[:-8].replace("_", ":")
    movies[os.path.basename(movie)[:-9].replace("_", ":")] = movie
    
# Adjust some titles:
movies["50/50"] = movies.pop("50:50")
movies["Face/Off"] = movies.pop("Face:Off")
movies["Frost/Nixon"] = movies.pop("Frost:Nixon")
    

#---------------------------------------------------------------------------------------------
# create main dataframe
movies_final = pd.DataFrame()
for key in movies:
    if key in movies_5000:
        temp = pd.read_csv(movies[key], usecols = ["username", "review"])
        temp.insert(1, "title", key)
        print(key)
        movies_final = pd.concat([movies_final, temp])
        
movies_final.reset_index()

#%% OUTPUT
"""
    movies_final dataframe is containing all reviews for 825 movies, that are 
    both in 5000 movies dataset and in reviews dataset. The columns in frame are:
        - username
        - title
        - review
"""
# whole dataframe export 
#movies_final.to_csv(os.path.join(path, "full_review_data.csv"))

#---------------------------------------------------------------------------------------------
# username - title dataframe export
movies_final[["username", "title"]].to_csv(os.path.join(path, "Network", "net_data.csv"), index = False)