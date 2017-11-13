from queue import Queue
import requests
import threading
from bs4 import BeautifulSoup
from settings import SENTINEL


class Scheduler(threading.Thread):
    def __init__(self, rss_queue):
        super().__init__()
        self.datascience_blogs = 'https://github.com/rushter/data-science-blogs'
        self.rss_queue = rss_queue

    def get_url_text(self, url):
        res = requests.get(url)
        # raise error if request fails
        res.raise_for_status()
        return res.text

    def extract_rss_urls(self, html):
        soup = BeautifulSoup(html, "html.parser")
        a_tags = soup.find_all('a')
        rss_urls = [tag['href'] for tag in a_tags if tag.string == '(RSS)']
        return rss_urls

    def push_list_to_queue(self, l, q):
        for item in l:
            q.put(item)

    def signal_queue_end(self, q, sentinel):
        q.put(sentinel)

    def run(self):
        html = self.get_url_text(self.datascience_blogs)
        rss_urls = self.extract_rss_urls(html)
        self.push_list_to_queue(rss_urls, self.rss_queue)
        self.signal_queue_end(self.rss_queue, SENTINEL)