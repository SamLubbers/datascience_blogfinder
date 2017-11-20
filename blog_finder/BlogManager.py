"""analyzes the extracted blogs and decides which get stored in the database"""
import threading
import json
import re
import pytz
from datetime import datetime, timedelta
from urllib.parse import urlparse
from blog_finder.settings import SENTINEL
from database.DatabaseManager import DatabaseManager
from blog_classifier.classify_blog import is_datascience_blog

class BlogManager(threading.Thread):
    """
    thread that gets information about a new blog from blog_queue (link to blog, title, publication date...),
    and stores it in the database according to 2 criteria:
    1. the classifier must classify it as a data science blog
    2. the blog must have been posted less than a year ago
    """
    def __init__(self, blog_queue):
        super().__init__()
        self.blog_queue = blog_queue
        self.blogs_db_name = 'datascience_blogs.db'

    def pubdate_to_datetime(self, pub_date):
        """converts the pubdate extracted form the rss feed onto a python datetime object"""
        pub_date = pub_date.split(',')[1].lstrip() # trim pub_date deleting day of the week
        pub_date = re.sub(' +', ' ', pub_date) # remove duplicate spaces
        timezone = pub_date.split(' ')[4]
        if '+' not in timezone and '-' not in timezone:
            dt = datetime.strptime(pub_date, '%d %b %Y %H:%M:%S')
        else:
            dt = datetime.strptime(pub_date, '%d %b %Y %H:%M:%S %z')
        # convert datetime to localtime
        dt = pytz.utc.normalize(dt.astimezone(pytz.utc))  # transform time to UTC
        dt = dt.replace(tzinfo=None) # eliminate timezone info to store in db
        return dt

    def parse_blog(self, blog_json):
        """
        parses the blog data to the format in which it is stored in the database
        :param blog_json: json object with url to blog and associated metadata
        :return: dictionary representing an instance in the blogs table of the database
        """
        blog = json.loads(blog_json)
        blog['host'] = urlparse(blog['url']).hostname
        blog['pub_date'] = self.pubdate_to_datetime(blog['pub_date'])
        return blog

    def recent_blog(self, blog_pubdate):
        """returns true if the blog publication date less than a year ago"""
        timezone = blog_pubdate.tzinfo
        now_in_timezone = datetime.now(timezone)
        one_year_ago = now_in_timezone - timedelta(days=365)
        if blog_pubdate >= one_year_ago:
            return True

        return False

    def run(self):
        db_mngr = DatabaseManager(self.blogs_db_name)
        for blog in iter(self.blog_queue.get, SENTINEL):
            try:
                blog = self.parse_blog(blog)
            except Exception:
                pass  # if exception occurs while parsing simply do not store blog in the db
            else:
                if is_datascience_blog(blog['title']) and self.recent_blog(blog['pub_date']):
                    db_mngr.insert_blog(url=blog['url'],
                                        host=blog['host'],
                                        title=blog['title'],
                                        pub_date=blog['pub_date'])

        db_mngr.delete_old_blogs()