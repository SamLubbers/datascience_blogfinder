"""Manual labelling of all blogs stored in the database

For every blog in the database it prints the title and the user labels it.
Results are stored in a csv file, which will be used as the dataset to train
and test the classifier.

Run only if dataset does not exist yet and you need to create data to train the classifier
"""
from os import path
import csv
from database.DatabaseManager import DatabaseManager

blogs_db_name = 'datascience_blogs.db'
csv_name = 'labelled_blogs.csv'
datasets_dir = 'datasets'
csv_path = path.join(datasets_dir, csv_name)

def create_csv():
    """creates the csv file where the data will be stored"""
    if not path.exists(csv_path):
        with open(csv_path, 'w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(['title', 'is_datascience_blog'])

def get_blogs():
    """gets all stored blogs in the database"""
    db_mngr = DatabaseManager(blogs_db_name)
    return db_mngr.get_all_blogs()

def label_title(title):
    """gets user input in order to label a blog as data science/not data science"""
    labelled_blog = {}
    print(title)
    label = input('is datascience blog? (1/0) ')
    labelled_blog['title'] = title
    labelled_blog['is_datascience_blog'] = label
    return labelled_blog

def update_csv(labelled_blog):
    """inserts a new row in the csv file with the title and associated label"""
    with open(csv_path, 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([labelled_blog['title'], labelled_blog['is_datascience_blog']])

if __name__ == '__main__':
    create_csv()
    blogs = get_blogs()
    for blog in blogs:
        blog_title = blog[2]
        labelled_blog = label_title(blog_title)
        update_csv(labelled_blog)

