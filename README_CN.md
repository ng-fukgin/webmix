
web\_utils.py 库: 为Web请求提供统一解决方案
===============================
[English Documentation](README.md) | [中文文档](README_CN.md)

> **请注意:**
> 如果中文文档和英文文档有冲突，请以英文文档为主。

在数字时代，数据从未如此重要。每天，开发者、数据科学家和业务分析师都在努力从Web上获取、分析和利用数据。然而，当前的Web请求库种类繁多，每个库都有其独特的接口和使用方法。这不仅使得学习和切换成本变得很高，还为代码引入了复杂性和不稳定性。

**WebFetcher** 库的诞生源于对统一、高效和简便的Web请求解决方案的渴望。无论你背后使用的是requests、urllib还是Selenium，**WebFetcher** 为你提供了一个统一的、简洁的接口。这意味着你可以在不更改任何核心代码的情况下自由切换后端技术，保证了代码的可读性和可维护性。

但这仅仅是我们的第一步。我们相信，为了使这个库真正具有影响力和广泛的应用，社区的力量是必不可少的。无论你是新手还是资深开发者，我们都诚挚地邀请你参与到这个项目中来。不仅可以通过提交代码和改进功能来贡献，还可以通过分享你的使用经验和建议来帮助我们。只有大家携手合作，**WebFetcher** 才能真正成为每个开发者工具箱中的必备工具。

如果你对Web开发充满热情，对创新和卓越有着不懈的追求，那么请加入我们！让我们共同打造一个强大、灵活且易于使用的Web请求库，为全球的开发者提供服务。



`web_utils.py` 包含一个名为 **WebFetcher** 的类，该类提供多种方法用于抓取网络内容。

导入
--
```
import requests
from urllib import request, parse, error
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
```

WebFetcher 类
------------

### 初始化
```
def __init__(self, backend='requests'):
    self.backend = backend
    self.driver = None
 ```

使用 backend 参数（默认值为 'requests'）初始化 WebFetcher 类。

### 请求
```
def request(self, method, url, **kwargs):
    ...
```

发送HTTP请求。支持的方法有 GET、POST、PUT 和 DELETE。可以使用 'requests', 'urllib' 或 'selenium' 作为后端来发送请求。

### Selenium 助手方法


*   **fill\_form\_by\_id**: 根据ID填写表单元素
*   **click\_button\_by\_id**: 根据ID点击按钮
*   **scroll\_to\_bottom**: 滚动到页面底部
*   **execute\_script**: 执行JavaScript脚本

### 关闭
```
def close(self):
    ...
```

如果使用了 Selenium 作为后端，此方法会关闭 WebDriver 会话。

### HTTP方法

*   **get**: 发送GET请求
*   **post**: 发送POST请求
*   **put**: 发送PUT请求
*   **delete**: 发送DELETE请求

这些方法是 **request** 方法的简便形式，用于发送指定的HTTP请求。



使用 `WebFetcher` 类的示例
--------------------

### 使用 requests 作为后端
```
from web_utils import WebFetcher

fetcher = WebFetcher(backend='requests')
response = fetcher.get("https://example.com")
print(response)

```

### 使用 urllib 作为后端

```
fetcher = WebFetcher(backend='urllib')
response = fetcher.get("https://example.com")
print(response)
```

### 使用 selenium 作为后端
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