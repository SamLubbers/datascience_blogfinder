from blog_classifier.classifier import corpus, process_title, classifier
from sklearn.feature_extraction.text import CountVectorizer

def title_to_vector(title):
    cv = CountVectorizer(max_features=80)
    extended_corpus = corpus + [title]
    all_titles_vector = cv.fit_transform(extended_corpus).toarray()
    title_vector_index = all_titles_vector.shape[0] - 1
    title_vector = all_titles_vector[title_vector_index, :].reshape(1, -1)
    return title_vector

def classify_datascience_blog(title):
    title = process_title(title)
    title = title_to_vector(title)
    is_datascience_blog = classifier.predict(title)
    return is_datascience_blog[0]

if __name__ == '__main__':
    prediction = classify_datascience_blog(input('enter blog name: '))

    if prediction:
        print('this is a data science blog')
    else:
        print('this is not a data science blog')
