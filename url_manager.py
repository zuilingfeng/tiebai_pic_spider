
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)

    def get_new_url(self, count, url):
        return url + "?pn=%d"%count
