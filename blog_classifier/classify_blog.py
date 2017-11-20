"""classifies a new blog title as data science or not"""
from blog_classifier.classifier import corpus, process_title, classifier
from sklearn.feature_extraction.text import CountVectorizer


def title_to_vector(title):
    """converts a blog title onto a vector of the shape expected by the classifier"""
    cv = CountVectorizer(max_features=1500)
    extended_corpus = corpus + [title]
    all_titles_vector = cv.fit_transform(extended_corpus).toarray()
    title_vector_index = all_titles_vector.shape[0] - 1
    title_vector = all_titles_vector[title_vector_index, :].reshape(1, -1)
    return title_vector


def is_datascience_blog(title):
    """
    predicts if the given title of a blog corresponds to the category of data science
    :param title: string representing a blog title
    :return: 1 if the title corresponds to a data science blog, 0 if not
    """
    title = process_title(title)
    title = title_to_vector(title)
    prediction = classifier.predict(title)
    return prediction[0]
