"""web scraping of blogs from rss feeds"""
import json
import threading
import requests
from bs4 import BeautifulSoup
from blog_finder.settings import SENTINEL
from blog_finder.update_sources import remove_invalid_sources

class BlogExtractor(threading.Thread):
    """
    thread that gets a link to an rss feed from the rss_queue, scraps all the blogs contained in that link,
    and pushes all those links to the blog_queue
    """
    def __init__(self, rss_queue, blog_queue):
        super().__init__()
        self.rss_queue = rss_queue
        self.blog_queue = blog_queue

    def get_url_text(self, url):
        """get request to the rss feed link"""
        res = requests.get(url, timeout=5)
        # raise error if request fails
        res.raise_for_status()
        return res.text

    def extract_blogs_from_rss(self, rss):
        """webscraping of rss feed"""
        blogs = []
        soup = BeautifulSoup(rss, 'xml')
        items = soup.find_all('item')
        for item in items:
            blog_contents = {}
            blog_contents['title'] = str(item.title.string)
            blog_contents['url'] = str(item.link.string)
            blog_contents['pub_date'] = str(item.pubDate.string)
            blogs.append(json.dumps(blog_contents))
        return blogs

    def push_list_to_queue(self, l, q):
        for item in l:
            q.put(item)

    def signal_queue_end(self, q, sentinel):
        q.put(sentinel)

    def run(self):
        invalid_rss_urls = []
        for rss_url in iter(self.rss_queue.get, SENTINEL):
            try:
                rss = self.get_url_text(rss_url)
                blogs = self.extract_blogs_from_rss(rss)
            except Exception as err:
                # if some url does not work or scraping fails catch error and
                # add it to the list of invalid_urls in order for it to be removed from the list of sources
                invalid_rss_urls.append(rss_url)
            else:
                # if no error occurs push link to blog to the blog_queue
                self.push_list_to_queue(blogs, self.blog_queue)

        remove_invalid_sources(invalid_rss_urls)
        self.signal_queue_end(self.blog_queue, SENTINEL)
