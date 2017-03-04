#--coding:utf-8
from urllib import request

def getHtml(baseUrl):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36'
    }
    page = 2
    url = baseUrl + str(page)
    zhihuurl = "https://www.zhihu.com/question/29457212"
    try:
        req = request.Request(url, None, header)
        response = request.urlopen(req, timeout=3000)
        html = response.read().decode('UTF-8', 'ignore')
        # 正则表达式
        import re
        pattern = re.compile(
            # r'<div class="author clearfix">[\s\S]*?<h2>(.*?)</h2>',re.S)
            #r'<div class="author clearfix">[\s\S]*?<h2>(.*?)</h2>[\s\S]*?<div class="content">([\s\S]*?)</div>',re.S)
            r'<div class="author clearfix">[\s\S]*?<h2>(.*?)'
            r'</h2>[\s\S]*?<div class="content">[\s\S]*?<span>([\s\S]*?)'
            r'</span>[\s\S]*?<i class="number">(.*?)</i>',re.S)

        items = re.findall(pattern, html)
        for item in items:
            print(item[0])
            print(item[1])
            print(item[2])
        response.close()
    except request.URLError as e:
        print(e)
    return html


if __name__ == '__main__':
    baseUrl = "http://www.qiushibaike.com/hot/page/"
    html = getHtml(baseUrl)
    path = "sourcehtml.txt"
    # with open(path, 'wt') as f:
    #     f.write(html)
    # print(html)

