# Python Baidu Search API
自己手写的百度搜索接口的封装，pip安装，支持命令行执行。
Unofficial Baidu Search API for Python.

It uses web scraping in the background and is compatible with both **Python 2 and 3**.


## Source
https://github.com/amazingcoderpro/python-baidusearch


## Why this project?

for everyone who want to use baidu search.


## Features

* Free unrestricted API, requires no key or credit card
* Unicode support
* Works for all Python versions (2 & 3)


## Installation

```sh
pip install baidusearch
```



## Using

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


## Examples

```sh
>>> from baidusearch.baidusearch import search
>>> search('Python')
[{'title': 'Welcome to Python.org官网', 'abstract': "The official home of the Python Programming Language...  # Python 3: List comprehensions >>> fruits = ['Banana', 'Apple', 'Lime'] >>> loud_fruits ...", 'url': 'http://www.baidu.com/link?url=cwYxPdTt2BvutAY8dyUXTmkaWD0dkOHxqdXx4Yf12cEz4QtxP20DS2V76sM02UiV', 'rank': 1}, {'title': 'Python_百度百科', 'abstract': 'Python是一种计算机程序设计语言。是一种面向对象的动态类型语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型...   \n                \n\nPython简介及应用领域\n下载Python\n发展历程\n风格\n更多>>\n\nbaike.baidu.com/', 'url': 'http://www.baidu.com/link?url=VTtKogGlo04HC6OXufls8bARa00Sa6qqqFMiDVH8ElzbawCkliIA5GnslVHDTQldiZ6GLw6b0qWZn9CvPutoBK', 'rank': 2}, {'title': '2019年4 个关于 Python 编程语言的故事_WatchStor.com - 领先的...', 'abstract': '1天前\xa0-\xa0今天要讲 4 个关于 Python 编程语言的故事,来看看人工智能时代爆发的 Python。在这里先不告诉你 Python 是“最好的编程语言”(无论什么意思)。言归...', 'url': 'http://www.baidu.com/link?url=N6pJDdnll5vz4wePXeAFbuCCVeG80fx1-7TYR4AIc65RhvUs2xLSNz7tR3jWlDQGGN9jN9NXK3Oi6vFJjlSlWa', 'rank': 3}, {'title': 'Python教程 - 廖雪峰的官方网站', 'abstract': '2019年4月10日\xa0-\xa0研究互联网产品和技术,提供原创中文精品教程... 这是小白的Python新手教程,具有如下特点:中文,免费,零起点,完整示例,基于最新的Python 3版本。Python是一种计算机程序...', 'url': 'http://www.baidu.com/link?url=zALhNq5-wC0_-0n7D9wCOY7DbkgiDp34Vax4nDIqOdQUTDRCcjxtNyDt28PEWAVBiYq13wEh2YPXzYdHZBzCKdxjEYxZruTifOsDSxGXAnAgcDjSTrQLZa64tOVROQSh', 'rank': 4}, {'title': 'Github标星2w+,热榜第一,如何用Python实现所有算法-新闻频道-和讯网', 'abstract': '1天前\xa0-\xa0 学会了Python基础知识,想进阶一下,那就来点算法吧!毕竟编程语言只是工具,结构算法才是灵魂。  新手如何入门Python算法?  几位印度小哥在GitHub上建了...', 'url': 'http://www.baidu.com/link?url=DFhvfJkV-Mkf5kos9ZU0HXTd8TIePKRBVYFvsTuIQ4C8e8FpsvjWLf8xcZ0Y5DQFhupRKgjkir9TqqqV3EMFiq', 'rank': 5}, {'title': 'Python 简介 | 菜鸟教程', 'abstract': 'Python 简介 Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。 Python 的设计具有很强的可读性,相比其他语言经常使用英文关键字,其他语言...', 'url': 'http://www.baidu.com/link?url=2kup-3yNhTL4TZtIGh4dij0T_by-RrpZhtQyTdLxdPBhkU1QyCftZ_u40B57kjw1pbqCVr855cIlP4COGEdPWq', 'rank': 6}, {'title': '这里有8个流行的Python可视化工具包,你喜欢哪个?_凤凰网科技', 'abstract': '1天前\xa0-\xa0喜欢用 Python 做项目的小伙伴不免会遇到这种情况:做图表时,用哪种好看又实用的可视化工具包呢?之前文章里出现过漂亮的图表时,也总有读者在后台留言...', 'url': 'http://www.baidu.com/link?url=AvonuOcAHDHMPhw-kotE-mKtfVmWpX3OfzWfkwwbM60Qw4Le5m82aP1gZ3iKhSS9', 'rank': 7}, {'title': 'Download Python | Python.org', 'abstract': 'The official home of the Python Programming Language... Looking for Python with a different OS? Python for Windows, Linux/UNIX, Mac OS X, Other ...', 'url': 'http://www.baidu.com/link?url=jvryi70Hj3_XYdUYI7n1Q1x35kUP2-ZicozQ2MIKyEBG2kLgYHRGxfFYW-bAK3-o', 'rank': 8}, {'title': 'Python_官方电脑版_华军纯净下载', 'abstract': '版本 : 3.7.3 for Windows\n 大小 : 24.25MB\n 更新 : 2019-04-17\n 环境 : WinAll\n\n立即下载', 'url': 'http://soft.onlinedown.net/soft/14542.htm', 'rank': 9}, {'title': 'Python - 开源软件 - OSCHINA', 'abstract': 'Pytype 是 Google 开源的 Python 静态类型分析器。 Pytype 可以: Lint plain Python code, flagging common mistakes s... 收藏0 评论0  Pyright - Python ...', 'url': 'http://www.baidu.com/link?url=25WmCBMCAtbxafgNDexDO2U-O4BSOaYeA8UnBKMqUos5ovD8WeM5P96Huw88tztwrsS_xA98qLkKhHRC9Ea1j_', 'rank': 10}]

>>>
>>> search('Baidu Search API', num_results=15)
[{'title': '百度数据开放平台', 'abstract': '百度金融 免费开放收录财经类网站的金融信息数据 查看详情 百度本地生活 面向APP、网站、自媒体等免费开放收录商户信息、探店攻略等数据 查看详情 百度游戏 免费开放...', 'url': 'http://www.baidu.com/link?url=Ch4KZ7bsaseEDmu5i93jirQnw4UMTfDTl2yIwd6JEj0LUzXOJKBi2Nvy2ZYzSX3G', 'rank': 1}, {'title': '百度站内搜索_最专业的站内搜索工具', 'abstract': '百度站内搜索旨在帮助站长低成本地为网站用户提供高质量的网站内搜索服务。使用百度站内搜索工具,您可以轻松打造网站专属的搜索引擎,自定义个性化的展现样式、功能模块...', 'url': 'http://www.baidu.com/link?url=YQ7G_LSQZiQyMsRIglJjoBjgUq-dzHuAaVtYQQ8Hyalvx44tki7jwZV8xluiual6', 'rank': 2}, {'title': '百度地图api-查询周边 - 热爱世界的liang - 博客园', 'abstract': '2019年4月1日\xa0-\xa0利用百度地图api接口实现周边配套设施查询 1. 静态页面部分: 1  2  3 ...click="baiduMapSearch(\'公交\')">交通设施 7 ...', 'url': 'http://www.baidu.com/link?url=Y0AQYCiFryr8r0dTEV6kaANHctpMnogtkXIPfj05nyBsg8CXFOxHgS5QKi0dhVnAyEF_FuBtBhUzHLGxukbRVK', 'rank': 3}, {'title': '百度地图开放平台 | 百度地图API SDK | 地图开发', 'abstract': '百度地图API是一套为开发者提供的基于百度地图的应用程序接口,包括JavaScript、iOS、Andriod、静态地图、Web服务等多种版本,提供基本地图、位置搜索、周边搜索、公交...', 'url': 'http://www.baidu.com/link?url=rcGZrXHLYsQgBvKvU22AKMfQDYZgqaq3yMh5OIiKTif6bgVoBWQfH3BldooM2Xfm', 'rank': 4}, {'title': 'Web服务Place API', 'abstract': 'http://api.map.baidu.com/place/search?&query=关键字&bounds=查询区域&output=输出格式类型&key=用户密钥 接口参数 参数是否必须默认值格式举例含义 query(q) ...', 'url': 'http://www.baidu.com/link?url=JPJcw8-ce4zah5RhEFWdiP8v-B5J3dD1Il3GyI5DiaasGslsu9XZod7al3k1zxwmxielIJcfWGY74QkMAZVI7_', 'rank': 5}, {'title': '百度地图JSAPI 2.0类参考', 'abstract': '2018年9月9日\xa0-\xa0LocalSearch LocalSearchOptions CustomData RenderOptions LocalResult LocalResult...此常量表示API版本号,通过字符串进行描述。  常量 常量 描述 B...', 'url': 'http://www.baidu.com/link?url=8QiwaREHn0I2_3Pb4SwJqV_VR0M8PvZSXxeZ1u3ipW8sZbMVD23nwfX6N3VdieL5gdyaWLBog2v6FlDZHkxcZMLXFh8-vYBtlz9tr_HX9Ii', 'rank': 6}, {'title': '百度地图没有com.baidu.mapapi.search.geocode包了怎么..._百度知道', 'abstract': '最佳答案: 如何在页面中调用百度地图,直接在你想要插入的页面上调用百度地图代码即可百度地图调用API地址:1.设置定位中心:直接搜索你要找的位置即可。调用百度地图代码...更多关于Baidu Search API的问题>>', 'url': 'http://www.baidu.com/link?url=x34veV2k8hXm1bmMYL5B1PK0l5A9IvUtf_OMbe-C8lTkTP6RCnvCD7xQIkDFjzmGoa-W4MgRDidqyihiURg67LE6x3rV19gXVmz7bfSdBly', 'rank': 7}, {'title': 'Baidu Search API的中文翻译_百度翻译', 'abstract': '.op_sp_fanyi{font-size:1em;word-break:normal;}\n    .op_sp_fanyi .op_sp_fanyi_read{display: inline-block;*display: inline;*zoom:1;margin-left:4px;*position:relative;*top:-2px;}\n    .op_sp_fanyi_how_read,.op_sp_fanyi_mp3_play{display:block;width:14px;height:11px;overflow:hidden;background: url(https:/', 'url': 'http://www.baidu.com/link?url=GdT_lFCClh_Yjq_vI9rjgYk6FnLhXDSszY25gOyvCczePXQ3bHtM0LdiR_grpRFoC1FaKj25JYg2wlg1Zklgz3YhFVKxqST9XV_MyV9khaa', 'rank': 8}, {'title': '首页- 百度地图API', 'abstract': '出自百度地图API跳转到: 导航 , 搜索 核心类 基础类 控件类 覆盖物类 工具类 右键菜单类 地图类型类 地图图层类 服务类 全景类 Map PanOptions MapOptions ...', 'url': 'http://www.baidu.com/link?url=YbupDpfeEIfz7wW3MBzTQqOGsn3prp_pXRTkrpiK5BQot7uvphmB9s6hyEb-dE_-KORYMExKlUrfrIiKVBfiFfNw8bljIW0Mq6S1QTXK8x7', 'rank': 9}, {'title': '百度图片-发现多彩世界', 'abstract': '百度图片使用世界前沿的人工智能技术,为用户甄选海量的高清美图,用更流畅、更快捷、更精准的搜索体验,带你去发现多彩的世界。', 'url': 'http://www.baidu.com/link?url=XiqriTkuL03F-JE74gTGxsWha42Cct2VXrSzoqZQBtwuS2pKqfbBOS-aHzIXYQQF', 'rank': 10}, {'title': '百度地图api-查询周边 - 热爱世界的liang - 博客园', 'abstract': '2017年10月25日\xa0-\xa0click="baiduMapSearch(\'公交\')">交通设施 7 ...· 百度地图IP对应的API查询· 百度地图简单地图api· 基于Mapabc API的周边查询应用 最新新闻:· 腾讯王巨宏...', 'url': 'http://www.baidu.com/link?url=gaLC_r1e0UsHM6ySJbJhAaK1ToeIReZWIO6hPIVdkfetbTZ43iyuFxFsG_yPO71ahp0SFNavbpieH4s4xHVRoa', 'rank': 11}, {'title': '百度API 常用接口demo - nankiao的博客 - CSDN博客', 'abstract': '2017年9月15日\xa0-', 'url': 'http://www.baidu.com/link?url=t-0eA8AGGRWQ_MQpHfqZx0EHu5kB_HsiDtFkGAkwQlS6yKxfwlBngp2JonWyST_6eLlA5NYx6uiPd0ql2R3zha', 'rank': 12}, {'title': '百度搜索风云榜', 'abstract': '9 戴姆勒主管道歉 62888 search  10 十城限售令到期 61427 search  完整榜单  汽车 更多>  < > 汽车  排名 关键词 关注度 1 ...', 'url': 'http://www.baidu.com/link?url=qDqh0W9QJ67qZz2ISRlyaE0k3D8-TixdoRbUHr7QvzG', 'rank': 13}, {'title': '百度Elasticsearch', 'abstract': '百度Elasticsearch帮助文档... 搜索RefererAPI 百度舆情API  客群洞察  百度信息流推广API  搜索...百度Elasticsearch 是一项托管服务,让您可以在百度智能云中轻松地...', 'url': 'http://www.baidu.com/link?url=4RWNXHV4dteW0-THEwYykizyz2jU8rdKUbKUhI_Rx9nTQUkFgYEyD4y_aEOEq1CSLe8tIaqmY5RR8JfkObgj0_', 'rank': 14}, {'title': '百度站内搜索https不可用切换api搜索,加上谷歌api站内..._CSDN博客', 'abstract': "2019年1月11日\xa0-\xa0\xa0\xa0\xa0\xa0var\xa0cse\xa0;\xa0\xa0\xa0\xa0//参数为您的API引擎ID,已自动填写,必需。\xa0\xa0\xa0\xa0var\xa0form=document.querySelector('searchBaidu-bd')...", 'url': 'http://www.baidu.com/link?url=F1_eDPSyTNpPR43gl7kj5tPGHB_o5xquAS6EzPzrf_8NKEDt3NOMW1gVIo6w3i0uE9IZwgYJlxS9ZtHUgic7wyGX-CfgiuJhZ-5Vd2Lsw5m', 'rank': 15}]

```


## Warning

Overusing this library might lead to your IP being blocked by Baidu Search servers.
Searches through Chrome or another browser might still work but this library will stop working.
I recommend keeping a 15 seconds gap after each usage of this library.
In most cases, much lower gaps or even continuous use of the library will still work but still this is something to be kept in mind.
If you see a 'rate limit' or a 503 error, it's best to stop using the library and try back after some time (~1 minute).


