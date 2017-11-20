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



from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=1000)

X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

correct_negative_predictions = cm[0, 0]
correct_positive_predictions = cm[1, 1]
total_correct_predictions = correct_negative_predictions + correct_positive_predictions
test_set_size = len(y_test)

accuracy = total_correct_predictions / test_set_size

print(accuracy)

