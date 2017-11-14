import threading
from blog_finder.settings import SENTINEL, SOURCES_FILE

class Scheduler(threading.Thread):
    def __init__(self, rss_queue):
        super().__init__()
        self.rss_queue = rss_queue

    def get_rss_urls(self, file_name):
        urls = []
        with open(file_name, 'r') as file:
            for line in file:
                line = line.rstrip('\n')
                urls.append(line)
        return urls

    def push_list_to_queue(self, l, q):
        for item in l:
            q.put(item)

    def signal_queue_end(self, q, sentinel):
        q.put(sentinel)

    def run(self):
        rss_urls = self.get_rss_urls(SOURCES_FILE)
        self.push_list_to_queue(rss_urls, self.rss_queue)
        self.signal_queue_end(self.rss_queue, SENTINEL)