"""updates the file containing the rss source links"""
from blog_finder.settings import SOURCES_FILE

def remove_invalid_sources(invalid_rss_urls):
    """deletes from the source file the specified link"""
    sources = []
    with open(SOURCES_FILE) as file:
        for line in file:
            sources.append(line)
    with open(SOURCES_FILE, 'w') as file:
        for source in sources:
            if not any(invalid_url in source for invalid_url in invalid_rss_urls):
                file.write(source)
            else:
                print('%s has been removed from sources' % source.rstrip('\n'))
