"""traning and testing of data science blog classifier

Given a set of blog titles and their associated labels, indicating if the blog corresponds to the topic of data science,
a naive bayes classifier is trained in order to predict if a future extracted blog is a data science blog
"""
from nltk.corpus import stopwords
import pandas as pd
from os import path, getcwd

datasets_dir = path.join(getcwd(), 'datasets')
dataset_name = 'labelled_blogs.csv'
dataset_path = path.join(datasets_dir, dataset_name)
dataset = pd.read_csv(dataset_path)

import re
import nltk
nltk.download('stopwords')

corpus = []

for index, blog in dataset.iterrows():
    title = blog['title']
    title = re.sub('[^a-zA-Z]', ' ', title)
    title = title.lower()
    title = title.split()
    title = [word for word in title if word not in set(stopwords.words('english'))]
    title = ' '.join(title)
    corpus.append(title)

title_labels = dataset.iloc[:, 1].values

# TODO create count vectorizer

# TODO create train and test datasets

# TODO create naive Bayes classifier

# TODO test performance of classifier




