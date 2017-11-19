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


def extract_top_words(all_words, n):
    """
    extract the top n words appearing in a list
    :param all_words: list of words
    :return: top n number of words
    """
    all_words_freq_dist = nltk.FreqDist(all_words) # create frequency distribution of all words
    word_frequencies = all_words_freq_dist.most_common(n)
    top_words = [word_frequency[0] for word_frequency in word_frequencies]
    return top_words

def feature_extractor(title, word_features):
    """
    converts a blog title to a bag of words, indicating if it contains the words specified by word_features
    :param title: title of a blog
    :param word_features: list of words composing the bag of words
    :return: bag of words, indicating which words this title contains
    """
    title_words = set(title.split())
    title_features = {}

    for word in word_features:
        title_features['contains({})'.format(word)] = (word in title_words)


    return title_features

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

    word_features = extract_top_words(all_words, 1000)
    
