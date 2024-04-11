
 web_utils.py 库: 为Web请求提供统一解决方案
===============================
[English Documentation](README.md) | [中文文档](README_CN.md)

**注意：** 如果中文文档和英文文档有冲突，请以英文文档为主。

## 介绍

在数字时代，数据从未如此重要。每天，开发者、数据科学家和业务分析师都在努力从Web上获取、分析和利用数据。然而，当前的Web请求库种类繁多，每个库都有其独特的接口和使用方法。这不仅使得学习和切换成本变得很高，还为代码引入了复杂性和不稳定性。

**WebFetcher** 库的诞生源于对统一、高效和简便的Web请求解决方案的渴望。无论你背后使用的是requests、urllib、http.client、aiohttp还是Selenium，**WebFetcher** 为你提供了一个统一的、简洁的接口。这意味着你可以在不更改任何核心代码的情况下自由切换后端技术，保证了代码的可读性和可维护性。

但这仅仅是我们的第一步。我们相信，为了使这个库真正具有影响力和广泛的应用，社区的力量是必不可少的。无论你是新手还是资深开发者，我们都诚挚地邀请你参与到这个项目中来。不仅可以通过提交代码和改进功能来贡献，还可以通过分享你的使用经验和建议来帮助我们。只有大家携手合作，**WebFetcher** 才能真正成为每个开发者工具箱中的必备工具。

如果你对Web开发充满热情，对创新和卓越有着不懈的追求，那么请加入我们！让我们共同打造一个强大、灵活且易于使用的Web请求库，为全球的开发者提供服务。

## 安装

你可以使用pip安装这个库:

```bash
pip install webmix
```
或者
```bash
pip3 install webmix
```

另外，你也可以从GitHub克隆这个仓库并手动安装:

```bash
git clone https://github.com/ng-fukgin/webmix
cd webmix
python setup.py install
```


使用 `WebFetcher` 类的示例

### 使用 `requests` 作为后端
```
from webmix.web_utils import WebFetcher

fetcher = WebFetcher(backend='requests')
response = fetcher.get("https://example.com")
print(response)
```     

### 使用 `urllib` 作为后端
```
fetcher = WebFetcher(backend='urllib')
response = fetcher.get("https://example.com")
print(response)
```
        

### 使用 `selenium` 作为后端
```
fetcher = WebFetcher(backend='selenium')
response = fetcher.get("https://example.com")
print(response)
 ```       

# 使用 Selenium 助手方法
```
fetcher.scroll_to_bottom()
fetcher.fill_form_by_id("myFormId", "Some Value")
fetcher.click_button_by_id("myButtonId")
script_output = fetcher.execute_script("return document.title;")
print(script_output)

fetcher.close()  # 关闭 WebDriver 会话
 ```       

请注意，使用 Selenium 可能需要额外的设置，例如安装相应的浏览器驱动。

### 使用 Selenium 的其他方法

WebFetcher 类为使用Selenium后端时与网页元素交互提供了很多帮助方法:

*   `find_element_by_id`: 通过其ID定位元素。

*   `find_element_by_name`: 通过其名字属性定位元素。
*   `find_element_by_xpath`: 使用XPath定位元素。
*   `wait_for_element_visibility`: 等待元素可见。
*   `switch_to_frame`: 切换焦点到特定的iframe或框架。
*   `switch_to_default_content`: 切换焦点回到主页面内容。
*   `switch_to_window`: 切换焦点到不同的浏览器窗口或选项卡。
*   `accept_alert`: 接受当前显示的警告框。
*   `dismiss_alert`: 关闭当前显示的警告框。
*   `maximize_window`: 最大化浏览器窗口。
*   `set_window_size`: 设置浏览器窗口的尺寸。

### 其他请求方法

WebFetcher还支持使用多种后端进行HTTP请求：

*   `_request_with_requests`: 使用requests库执行HTTP请求。
*   `_request_with_urllib`: 使用urllib库执行HTTP请求。
*   `_request_with_http_client`: 使用http.client库执行HTTP请求。
*   `_request_with_aiohttp`: 使用aiohttp库执行异步HTTP请求。

### 对其他库的支持

#### http.client 后端

```

fetcher = WebFetcher(backend='http_client')
response = fetcher.get("https://example.com")
print(response)
```

#### aiohttp 后端 (异步)

```

import asyncio

async def fetch_data():
    fetcher = WebFetcher(backend='aiohttp')
    response = await fetcher.get("https://example.com")
    print(response)

asyncio.run(fetch_data())
```

## 版本历史

| 版本  | 描述 |
|------|------|
| 0.0.4 | 基本功能的初始发布，工作如预期。 |
| 0.0.5 | 引入对`http.client`和`aiohttp`后端的支持。扩展了与Selenium集成的方法列表。 |
| 0.0.6 | 新增代理支持： 添加对代理的支持，以便在进行网络请求时可以使用代理服务器。 |



#   待实现功能：

- [ ] 用户代理随机化： 在请求时随机选择一个用户代理头，可以通过维护一个用户代理头列表来实现。
- [ ] Cookie 管理： 允许用户在请求中传递和管理 Cookie，可以通过 requests 库提供的 cookies 参数来实现。
- [ ] 连接池管理： 维护一个连接池以提高性能，可以使用 requests 库的 Session 对象来实现连接的重用。
- [ ] 自定义超时设置： 允许用户设置请求超时时间，可以通过 requests 库的 timeout 参数来实现。
- [ ] 重定向处理： 添加对重定向的支持，并提供选项来控制是否自动跟随重定向，可以使用 allow_redirects 参数来控制重定向。
- [ ] SSL 证书验证： 允许用户控制是否进行 SSL 证书验证，可以通过 requests 库的 verify 参数来实现。
- [ ] 日志记录： 添加日志记录功能，可以使用 Python 的内置 logging 模块来记录错误和警告信息。
- [ ] 用户界面交互： 提供交互式界面，可以考虑使用命令行交互或者图形界面库来实现。
- [ ] 并发请求支持： 添加并发请求支持，可以使用异步库（如 asyncio 和 aiohttp）来实现并发请求。
- [ ] 页面内容解析： 添加对页面内容的解析功能，可以使用解析库（如 BeautifulSoup、lxml 等）来实现。
- [ ] HTTP/2 支持： 如果需要，可以使用支持 HTTP/2 的库来实现 HTTP/2 支持。
- [ ] 自定义请求头： 允许用户设置自定义请求头，可以通过 headers 参数来实现。
- [ ] HTTP 认证支持： 添加对基本和摘要 HTTP 认证的支持，可以使用 auth 参数来实现。
- [ ] 数据缓存： 提供数据缓存功能，可以使用缓存库来实现，或者自行维护一个缓存系统。