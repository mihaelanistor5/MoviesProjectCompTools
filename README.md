# MoviesProjectCompTools
## dataset
- dataset_5000: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
- dataset_review: https://ieee-dataport.org/open-access/imdb-movie-reviews-dataset?fbclid=IwAR2bNdCgbWYldpFI4c9ttl3dxM0z7eCxabB4zCN7mK8r8MoBXrz7It8ee-8

## Network
- To run the Network part, simply go to Network folder and open ```Network.ipynb``` with use of Jupyter notebook. Don't open any data files, since autoformatting in some applications may alter the data, what will cause errors in the scripts.

## Sentiment
- The sentiment code is located in the code folder and is contained in the files labmt_sentiment.ipynb and VADER.ipynb. The labmt_sentiment.ipynb writes the two files labmt_sentiment.pkl (dataframe which contains all labmt sentiment data - including review text) and rating_and_sentiment.pkl files (subset of columns from labmt_sentiment.pkl). The new_num_review_users.pkl contains a pandas serie of all users and the number of reviews left. 
The VADER.ipynb writes the rating_and_sentiment_v2.pkl  file in the sentiment_dataset folder containing the  VADER sentiment scores.

## Collaborative Filtering
- The code for collaborative filtering recommender is located in the "Recommender_system" folder, and its name is "recommender_0112.ipynb". It write two files "rating_and_sentiment.pkl"(For rating and labMT sentiment score) and "rating_and_sentiment_v2.pkl"(for VADER sentiment score). Both of .pkl files are located in "sentiment_dataset" folder.
