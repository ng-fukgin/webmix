
web\_utils.py 库: 为Web请求提供统一解决方案
===============================
[English Documentation](README.md) | [中文文档](README_CN.md)

> **请注意:**
> 如果中文文档和英文文档有冲突，请以英文文档为主。

在数字时代，数据从未如此重要。每天，开发者、数据科学家和业务分析师都在努力从Web上获取、分析和利用数据。然而，当前的Web请求库种类繁多，每个库都有其独特的接口和使用方法。这不仅使得学习和切换成本变得很高，还为代码引入了复杂性和不稳定性。

**WebFetcher** 库的诞生源于对统一、高效和简便的Web请求解决方案的渴望。无论你背后使用的是requests、urllib还是Selenium，**WebFetcher** 为你提供了一个统一的、简洁的接口。这意味着你可以在不更改任何核心代码的情况下自由切换后端技术，保证了代码的可读性和可维护性。

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
--------------------

### 使用 requests 作为后端
```
from webmix.web_utils import WebFetcher

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