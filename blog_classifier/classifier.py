"""traning and testing of data science blog classifier

Given a set of blog titles and their associated labels, indicating if the blog corresponds to the topic of data science,
a naive bayes classifier is trained in order to predict if a future extracted blog is a data science blog
"""
import pandas as pd
from os import path, getcwd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def load_dataset(dataset_name):
    datasets_dir = path.join(getcwd(), 'datasets')
    dataset_path = path.join(datasets_dir, dataset_name)
    dataset = pd.read_csv(dataset_path)
    return dataset

def process_title(title):
    title = re.sub('[^a-zA-Z]', ' ', title)
    title = title.lower()
    title = title.split()
    title = [word for word in title if not word in set(stopwords.words('english'))]
    title = ' '.join(title)
    return title

# TODO remove duplicates by creating a frequency distribution and converting to list

# TODO create feature extractor that creates bag of words

# TODO create featuresets associating extracted features from titles to it's label

# TODO create train and test datasets

# TODO create naive Bayes classifier

# TODO test performance of classifier

if __name__ == '__main__':
    dataset = load_dataset('labelled_blogs.csv')
    processed_titles = []
    all_words = []
    for index, blog in dataset.iterrows():
        blog_title = blog['title']
        blog_title = process_title(blog_title)
        processed_titles.append(blog_title)
        for word in blog_title.split():
            all_words.append(word)
