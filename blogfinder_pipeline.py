from queue import Queue
from Scheduler import Scheduler
from BlogExtractor import BlogExtractor
from BlogManager import BlogManager

def main():
    rss_queue = Queue(10)
    blog_queue = Queue(100)
    scheduler = Scheduler(rss_queue)
    extractor = BlogExtractor(rss_queue=rss_queue, blog_queue=blog_queue)
    manager = BlogManager(blog_queue)

    scheduler.start()
    extractor.start()
    manager.start()

if __name__ == '__main__':
    main()