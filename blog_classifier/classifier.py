"""traning and testing of data science blog classifier

Given a set of blog titles and their associated labels, indicating if the blog corresponds to the topic of data science,
a naive bayes classifier is trained in order to predict if a future extracted blog is a data science blog
"""
from nltk.corpus import stopwords
import pandas as pd
from os import path, getcwd
import re
import nltk
nltk.download('stopwords')


def load_dataset(dataset_name):
    datasets_dir = path.join(getcwd(), 'datasets')
    dataset_path = path.join(datasets_dir, dataset_name)
    ds = pd.read_csv(dataset_path)
    return ds


def process_title(title):
    title = re.sub('[^a-zA-Z]', ' ', title)
    title = title.lower()
    title = title.split()
    title = [word for word in title if word not in set(stopwords.words('english'))]
    title = ' '.join(title)
    return title


# TODO create train and test datasets

# TODO create naive Bayes classifier

# TODO test performance of classifier

if __name__ == '__main__':
    dataset = load_dataset('labelled_blogs.csv')
    corpus = []
    for index, blog in dataset.iterrows():
        blog_title = blog['title']
        blog_title = process_title(blog_title)
        corpus.append(blog_title)

    title_labels = dataset.iloc[:, 1].values

    # TODO get rid of word features, all words etc.
    # TODO get rid of the below and replace by sklearn feature extractor
