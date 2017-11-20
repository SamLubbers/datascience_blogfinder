"""traning of data science blog classifier

Given a set of blog titles and their associated labels, indicating if the blog corresponds to the topic of data science,
a naive bayes classifier is trained in order to predict if a future extracted blog is a data science blog
"""
import pandas as pd
from os import path, getcwd

# load dataset
datasets_dir = path.join(getcwd(), 'blog_classifier', 'datasets')
dataset_name = 'labelled_blogs.csv'
dataset_path = path.join(datasets_dir, dataset_name)
dataset = pd.read_csv(dataset_path)

# create bag of words
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

corpus = []


def process_title(title):
    title = re.sub('[^a-zA-Z]', ' ', title)
    title = title.lower()
    title = title.split()
    title = [word for word in title if word not in set(stopwords.words('english'))]
    title = ' '.join(title)
    return title

for index, blog in dataset.iterrows():
    blog_title = blog['title']
    blog_title = process_title(blog_title)
    corpus.append(blog_title)

# convert bag of words onto a  of vectors
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=1500)

X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)