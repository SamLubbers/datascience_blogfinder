"""pipeline that puts together the complete blog_finder functionality

it instantiates 3 threads that work concurrently and uses 2 queues to coordinate the work between those threads
"""
from queue import Queue
from blog_finder.Scheduler import Scheduler
from blog_finder.BlogExtractor import BlogExtractor
from blog_finder.BlogManager import BlogManager

def main():
    print('extracting data science blogs from all over the internet, please wait until finished...')
    rss_queue = Queue(10)
    blog_queue = Queue(100)
    scheduler = Scheduler(rss_queue)
    extractor = BlogExtractor(rss_queue=rss_queue, blog_queue=blog_queue)
    manager = BlogManager(blog_queue)

    scheduler.start()
    extractor.start()
    manager.start()

    manager.join()
    print('blog extraction finished. You can view extracted blogs from the django frontend')

if __name__ == '__main__':
    main()