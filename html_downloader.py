
import urllib.request
import socket
import os
# timeout in seconds
timeout = 2
socket.setdefaulttimeout(timeout)
# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module

class HtmlDownloader(object):

    def downloader(self, url):
        if url is None:
            return None

        response =  urllib.request.urlopen(url)
        return response.read()

    def save_img(self, title, urls):
        if urls is None or len(urls) == 0 :
            return None

        pic_dir = "E:\Python\Picture" + "\\" + title
        if not os.path.exists(pic_dir):
            os.mkdir(pic_dir)

        i = 1001
        for url in urls:
            try:
                pic = urllib.request.urlopen(url)
            except:
                print("url:%s downloader failed"%url)

            name = pic_dir + "\\" + str(i) + ".jpg"

            fb = open(name, "wb")
            fb.write(pic.read())
            print("picture %d download complied"%i)
            fb.close()
            i = i + 1
