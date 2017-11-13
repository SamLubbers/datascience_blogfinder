import threading
from settings import SENTINEL


class BlogManager(threading.Thread):
    def __init__(self, blog_queue):
        super().__init__()
        self.blog_queue = blog_queue

    def run(self):
        for blog in iter(self.blog_queue.get, SENTINEL):
            # TODO store blogs in sqlite db
            print(blog)

