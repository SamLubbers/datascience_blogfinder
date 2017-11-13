import threading
import requests
from queue import Queue
from bs4 import BeautifulSoup
import json
from settings import SENTINEL

class BlogExtractor(threading.Thread):
    def __init__(self, rss_queue, blog_queue):
        super().__init__()
        self.rss_queue = rss_queue
        self.blog_queue = blog_queue

    def get_url_text(self, url):
        res = requests.get(url)
        # raise error if request fails
        res.raise_for_status()
        return res.text

    # TODO handle exception if rss has no items, must discard rss
    def extract_blogs_from_rss(self, rss):
        blogs = []
        soup = BeautifulSoup(rss, 'xml')
        items = soup.find_all('item')
        for item in items:
            blog_contents = {}
            blog_contents['title'] = str(item.title.string)
            blog_contents['link'] = str(item.link.string)
            blog_contents['pub_date'] = str(item.pubDate.string)
            blogs.append(json.dumps(blog_contents))
        return blogs

    def push_list_to_queue(self, l, q):
        for item in l:
            q.put(item)

    def signal_queue_end(self, q, sentinel):
        q.put(sentinel)

    def run(self):
        for rss_url in iter(self.rss_queue.get, SENTINEL):
            try:
                rss = self.get_url_text(rss_url)
                blogs = self.extract_blogs_from_rss(rss)
            except Exception as err:
                # if some url does not work or scraping fails ignore and proceed with next url
                pass
            else:
                # if no error occurs push link to blog to the blog_queue
                self.push_list_to_queue(blogs, self.blog_queue)

        self.signal_queue_end(self.blog_queue, SENTINEL)
