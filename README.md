# Python Baidu Search API

[![Version](https://img.shields.io/pypi/v/baidusearch.svg)](https://pypi.python.org/pypi/baidusearch)
[![GitHub](https://github.com/wcadaydayup/python-baidusearch.svg?branch=master)](https://https://github.com/wcadaydayup/python-baidusearch)

Unofficial Baidu Search API for Python.

It uses web scraping in the background and is compatible with both **Python 2 and 3**.


### Why this project?

for everyone who want to use baidu search.


### Features

* Free unrestricted API, requires no key or credit card
* Unicode support
* Works for all Python versions (2 & 3)


### Installation

```sh
pip install baidusearch
```



### Using

```sh
> from baidusearch.baidusearch import search

> results = search('Full Stack Developer')  # returns 10 or less results
[ {"title:'Name', "abstract':Link', "url": URL},
	{"title:'Name2', "abstract':Link2', "url": URL2},
	... ]

> results = search('China', num_results=20)  # returns 20 or less results
```

You can also use it as a CLI tool.

```sh
$ baidusearch 长风破浪小武哥

search results：(total[10]items.)
1. 【图片】无意中发现小武哥的男朋友【大叔控吧】_百度贴吧
   无意中发现小武哥的男..两个都都关注了好几年了,今天看见这个泐欭发的微博觉得眼熟才想起来和小武哥经常发的照片里的屋子一样,对比了下照片一模一样,两个人...
   http://www.baidu.com/link?url=Vr7zkg9x9qRBOADHeybXxrTJ_KaDRf-FaKu9rXsy5cP-LI5JvBxJZOrpkXRO13_v
2. 厦门小武哥全部小说在线阅读_厦门小武哥新书作品集推荐_书书网
   (微信公众平台:厦门小武哥 读者交流群459968982)...厦门小武哥全部完结小说 共0部厦门小武哥没有已经完结的小说厦门小武哥新书消息暂无厦门小武哥的新书消息 ...
   http://www.baidu.com/link?url=N6BTLEOpnjboAb1OXb0UqDc86ueN4DHvmY_Z1WH4VBGgKPBfwI6RAmwoZaK8jT4j2HBAOl2xGAt3_MDxnB_i1_
3. 动态VPS环境初始化配置 - 简书
   2019年4月10日 - 长风破浪小武哥 2019.04.10 11:20* 字数505 最近在做一个自动化项目,用到了动态VPS, 刚刚拿到一个新的VPS难免要对系统环境进行一番配置,特此记录...
   http://www.baidu.com/link?url=HkKpoTVH3RBBUfe8gX2C7k2OX2Ocrz1--XRclUWRiT5Ru9dJWGv6r1EjdG9iDBSV
4. 快手小武哥-原创-高清正版视频在线观看–爱奇艺
   2017年1月19日 - 快手小武哥是原创类高清视频,于2017-01-19上映,视频画面清晰,播放流畅,内容质量高。视频主要内容:快手小武哥。。
   http://www.baidu.com/link?url=m4p6N9wlrsBX9WQregWVDund-1W5h324HZlTT7HdGELPE39CPBpmNA6v8VnQ-sUu2Iuut5Egw8wYAamQK385SK
5. 小武哥,第一次见到,惊艳了!【枣庄吧】_百度贴吧
   小武哥,第一次见到,..来到店里说是吧友,后来打听了一下,是小武哥,真帅,他走了,我恋恋不舍的。
   http://www.baidu.com/link?url=_RDVp9UMoqxa2Zf3NEyEkDodqqVoqhdpT6ToA9_T1BTGGviE4iEdzq_UU5EbNGXX
6. 小武哥-原创-高清正版视频在线观看–爱奇艺
   2018年11月7日 - 小武哥是原创类高清视频,于2018-11-07上映,视频画面清晰,播放流畅,内容质量高。视频主要内容:韦家军。。
   http://www.baidu.com/link?url=XTH4psJz1ROcYVExwNN4EZXMO9KiVn2f8zaupJF-f_MouZMFcVup4PsY_No-SZpb1dwYJT93cR7XbISW889tLK
7. 小武哥的博客 - 左手程序右手诗
   心若在,梦就在,坚持就是胜利,小武加油!... 2014年7月12日 小武哥 没有评论  [latexpage] 上一篇文章《Finite Field Arithmetic》介绍了有限域上的运算,理解有限...
   http://www.baidu.com/link?url=81UOq351KNY0PQvmTJpYB_TwaopHTEHua_SM6GebYBfnhjZVsPKx4YtyDEHXqkI3
8. 厦门小武哥的全部小说_厦门小武哥作品全集在线阅读_看书啦
   (微信公众平台:厦门小武哥 读者交流群459968982) 各位书友要是觉得《花都最强狂龙》还不错的话请不要忘记向您QQ群和微博里的朋友推荐哦!花都最强狂龙最新章节,花都...
   http://www.baidu.com/link?url=FZsq-ExxEv2FbDog71vOO2glbl55fwNfQn28Rg39njPiAfOZRQk8gJ8D3atyOXU1
9. 小武哥的微博_腾讯微博
   2016年8月14日 - Hi,这是小武哥的腾讯微博,立即登录并收听,别错过TA的精彩内容! 申请开通 马上登录  小武哥 (@xiaowuge_HU)  山东青岛 就职于华东  老男人就是我 我就...
   http://www.baidu.com/link?url=aIBHueFwUn9Z6SrDOSM52GcaWtk7jungo_-q9q1eHGRwgxloNWVnzFI6PR3jwXk9
10. 正宗小武哥
   正宗小武哥手机拍儿子,效果不比相机差  全文链接  妻怀孕36周,留个纪念  全文链接  全文链接  登顶俯瞰圣彼得广场,如同钥匙孔一般。 全文链接  赶了个大早,...
   http://www.baidu.com/link?url=zZJfyfjZXgo8F3i7R0c82teCwGJh-PUciVPOk8ZJEoaeEUGbvDK2prZpu59mWMz4

```


### Examples

```sh
>>> from baidusearch.baidusearch import search
>>> search('Python')
[('Welcome to Python.org', 'https://www.python.org/'), ('Python (programming language) - Wikipedia', 'https://en.wikipedia.org/wiki/Python_(programming_language)'), ('Python tutorial - TutorialsPoint', 'https://www.tutorialspoint.com/python/'), ('Learn Python (Programming Tutorial for Beginners) - Programiz', 'https://www.programiz.com/python-programming'), ('Learn Python | Codecademy', 'https://www.codecademy.com/learn/learn-python'), ('Learn Python | Codecademy', 'https://www.codecademy.com/en/courses/learn-python/lessons/python-syntax/exercises/welcome'), ('Introduction · A Byte of Python', 'https://python.swaroopch.com/'), ('Solve Introduction Questions | Python | HackerRank', 'https://www.hackerrank.com/domains/python')]
>>>
>>> search('Baidu Search API', num_results=15)
[('Custom Search JSON/Atom API | Custom Search | Google Developers', 'https://developers.google.com/custom-search/json-api/v1/overview'), ('Custom Search | Google Developers', 'https://developers.google.com/custom-search/'), ('Using REST to Invoke the API | Custom Search | Google Developers', 'https://developers.google.com/custom-search/json-api/v1/using_rest'), ('Custom Search Engine - Google', 'https://www.google.com/cse/'), ('What are the alternatives now that the Google web search API has ...', 'https://stackoverflow.com/questions/4082966/what-are-the-alternatives-now-that-the-google-web-search-api-has-been-deprecated'), ('Is there an API for Google search results? - Quora', 'https://www.quora.com/Is-there-an-API-for-Google-search-results'), ('Fetch Google Search Results with the Site Search API - CtrlQ.org', 'https://ctrlq.org/code/20076-google-search-api'), ('Google Custom Search API | ProgrammableWeb', 'https://www.programmableweb.com/api/google-custom-search'), ('Google Search API Alternative | Webhose.io', 'https://webhose.io/google-search-api-alternative'), ('FAROO - Free Search API', 'http://www.faroo.com/hp/api/api.html'), ("Google's Ajax Search API | Search Engine Watch", 'https://searchenginewatch.com/sew/news/2056817/googles-ajax-search-api'), ('Search | GitHub Developer Guide', 'https://developer.github.com/v3/search/'), ('Using the Google SOAP Search API - SEO Chat', 'http://www.seochat.com/c/a/google-optimization-help/using-the-google-soap-search-api/')]
```


### Warning

Overusing this library might lead to your IP being blocked by Baidu Search servers.
Searches through Chrome or another browser might still work but this library will stop working.
I recommend keeping a 15 seconds gap after each usage of this library.
In most cases, much lower gaps or even continuous use of the library will still work but still this is something to be kept in mind.
If you see a 'rate limit' or a 503 error, it's best to stop using the library and try back after some time (~1 minute).


