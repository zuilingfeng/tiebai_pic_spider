from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #<img class="BDE_Image" pic_type="0" width="560" height="558" src="https://imgsa.baidu.com/forum/w%3D580/sign=eecdbd4389025aafd3327ec3cbefab8d/7a90d01373f0820265716abc40fbfbeda9641ba9.jpg">
        links = soup.find_all(class_="BDE_Image", src=re.compile(r'^https://imgsa.baidu.com.+jpg$'))
        for link in links:
            new_url = link['src']
            new_urls.add(new_url)
        return new_urls

    def get_max_page(self, html_cont):
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        #<a href="/p/5470951190?pn=11">尾页</a>
        link = soup.find('a', text="尾页")
        max_page = re.findall(r'pn=(.+?)">', str(link))

        print("max_page= %d"%int(max_page[0]))
        return int(max_page[0])

    def get_title(self, html_cont):
        #< h3 class ="core_title_txt pull-left text-overflow  " title="【美图】你是我漫山遍野的欢喜"
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        title_node = soup.find('h3')
        title = title_node.get_text()

        return title

    def parser(self, page_url, html_cont):

        soup =  BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(page_url, soup)

        return new_urls
