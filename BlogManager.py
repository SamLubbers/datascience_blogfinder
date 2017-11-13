import threading
from settings import SENTINEL
from DatabaseManager import DatabaseManager


class BlogManager(threading.Thread):
    def __init__(self, blog_queue):
        super().__init__()
        self.blog_queue = blog_queue
        self.db_mngr = DatabaseManager('datascience_blogs.db')

    def run(self):
        for blog in iter(self.blog_queue.get, SENTINEL):
            # TODO store blogs in sqlite db
            print(blog)

