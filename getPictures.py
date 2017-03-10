# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import urllib.request

URL_REG = re.compile(r'(http://[^/\\]+)', re.I)
IMG_REG = re.compile(r'<img[^>]*?src=([\'"])([^\1]*?)\1', re.I)

def download(dir, url):
    # 下载网页中的图片
    # dir 保存到本地的路径
    # url 网页url
    global URL_REG, IMG_REG
    if __name__ == '__main__':
        m = URL_REG.match(url)
        if not m:
            print('[Error] Invalid url:', url)
            return
        host = m.group(1)

        if not os.path.isdir(dir):
            os.mkdir(dir)

        # 获取html，提取图片url
        html = urllib.request.urlopen(url).read()
        print(html)
        html = html.decode('GBK') # python 3
        images = [item[1].lower() for item in IMG_REG.findall(html)]
        f = lambda path: path if path.startswith('http://') else \
            host + path if path.startswith('/') else url + '/'
        images = list(set(map(f, images)))
        print('[Info]Find %d images...' % len(images))

        # 下载图片,enumerate用于遍历列表中的下标和元素
        for idx, img in enumerate(images):
            name = img.split('/')[-1]
            path = os.path.join(dir, name)
            try:
                urllib.urlretrieve(img, path)
                print('[Info]Download(%d) image...url= %s' % (idx + 1, img))
            except BaseException:

                print("[Error]Can't download(%d): %s" % (idx + 1, img))

if __name__ == '__main__':
    dir = "D:\\workspace\\python\\Images"
    url = "http://www.58pic.com/yuanchuang/22782950.html"
    download(dir, url)
    print("Runing fine...")

