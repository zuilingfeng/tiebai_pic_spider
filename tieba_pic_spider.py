# coding:utf8
# First, just spider all picture from  given URL .

import url_manager, html_downloader, html_parser

class Spider_Main(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        #self.output = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        html_cont = self.downloader.downloader(root_url)
        max_page =  self.parser.get_max_page(html_cont)
        title = self.parser.get_title(html_cont)

        while count <= int(max_page):

            try:
                new_url = self.urls.get_new_url(count, root_url)
                html_cont = self.downloader.downloader(new_url)
                new_urls  = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)

                print("craw: page %d, url:%s complied! new_urls len %d"%(count, new_url, len(self.urls.new_urls)))
                count = count + 1
            except:
                print("craw: somethings wrong!")

        self.downloader.save_img(title, self.urls.new_urls)
        #self.output.output_html()


if __name__ == "__main__":
    root_url = input("Please input baidu tieba URL: ")
    #root_url = "https://tieba.baidu.com/p/5470951190"
    obj_spider = Spider_Main()
    obj_spider.craw(root_url)
