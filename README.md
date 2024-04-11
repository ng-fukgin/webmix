

# web_utils.py Library: Providing a Unified Solution for Web Requests

[English Documentation](README.md) | [中文文档](README_CN.md)

**Note:** If there is a conflict between the Chinese and English documents, please prioritize the English document.

## Introduction

In the digital age, data has never been more important. Every day, developers, data scientists, and business analysts are striving to retrieve, analyze, and leverage data from the web. However, there is currently a wide variety of web request libraries, each with its unique interface and usage methods. This not only makes learning and switching costly but also introduces complexity and instability into the code.

The birth of the **WebFetcher** library stems from the desire for a unified, efficient, and straightforward solution for web requests. Whether you are using requests, urllib, http.client, aiohttp, or Selenium under the hood, **WebFetcher** provides you with a unified and concise interface. This means you can freely switch backend technologies without altering any core code, ensuring code readability and maintainability.

But this is just our first step. We believe that community strength is essential to making this library truly influential and widely used. Whether you are a beginner or an experienced developer, we sincerely invite you to participate in this project. You can contribute not only by submitting code and improving features but also by sharing your usage experience and suggestions to help us. Only through cooperation can **WebFetcher** truly become an essential tool in every developer's toolbox.

If you are passionate about web development and have an unwavering pursuit of innovation and excellence, please join us! Let's work together to create a powerful, flexible, and user-friendly web request library that serves developers worldwide.

## Installation

You can install the package using pip:

```bash
pip install webmix
```
or
```bash
pip3 install webmix
```

Alternatively, you can clone the repository from GitHub and install it manually:

```bash
git clone https://github.com/ng-fukgin/webmix
cd webmix
python setup.py install
```


# Using the `WebFetcher` Class

### Using `requests` as the Backend
```
from webmix.web_utils import WebFetcher

fetcher = WebFetcher(backend='requests')
response = fetcher.get("https://example.com")
print(response)
```      

### Using `urllib` as the Backend
```
fetcher = WebFetcher(backend='urllib')
response = fetcher.get("https://example.com")
print(response)
 ```       

### Using `selenium` as the Backend
```
fetcher = WebFetcher(backend='selenium')
response = fetcher.get("https://example.com")
print(response)
  ```      

## Selenium Helper Methods
```
fetcher.scroll_to_bottom()
fetcher.fill_form_by_id("myFormId", "Some Value")
fetcher.click_button_by_id("myButtonId")
script_output = fetcher.execute_script("return document.title;")
print(script_output)

fetcher.close()  # close the `WebDriver` session
```    

Note that using Selenium may require additional setup, such as installing the appropriate browser driver.

### Additional Methods with Selenium

The `WebFetcher` class provides a host of helper methods to facilitate interaction with web elements when using the Selenium backend:

*   `find_element_by_id`: Locate an element by its ID.
*   `find_element_by_name`: Locate an element by its name attribute.
*   `find_element_by_xpath`: Locate an element using XPath.
*   `wait_for_element_visibility`: Wait for an element to be visible.
*   `switch_to_frame`: Switch the focus to a particular iframe or frame.
*   `switch_to_default_content`: Switch focus back to the main page content.
*   `switch_to_window`: Switch focus to a different browser window or tab.
*   `accept_alert`: Accept the currently displayed alert box.
*   `dismiss_alert`: Dismiss the currently displayed alert box.
*   `maximize_window`: Maximize the browser window.
*   `set_window_size`: Set the dimensions of the browser window.

### Other Request Methods

`WebFetcher` also supports making HTTP requests with a variety of backends:

*   `_request_with_requests`: Execute an HTTP request using the requests library.
*   `_request_with_urllib`: Execute an HTTP request using the urllib library.
*   `_request_with_http_client`: Execute an HTTP request using the http.client library.
*   `_request_with_aiohttp`: Execute an asynchronous HTTP request using the aiohttp library.

### Support for Other Libraries

#### http.client Backend

```

fetcher = WebFetcher(backend='http_client')
response = fetcher.get("https://example.com")
print(response)
```

#### aiohttp Backend (Asynchronous)

```

import asyncio

async def fetch_data():
    fetcher = WebFetcher(backend='aiohttp')
    response = await fetcher.get("https://example.com")
    print(response)

asyncio.run(fetch_data())
```

## Version History

| Version | Description |
|---------|-------------|
| 0.0.4   | Initial release with basic functionalities working as expected. |
| 0.0.5   | Introduced support for `http.client` and `aiohttp` backends. Extended the list of methods available for Selenium integration. |
| 0.0.6   | Added Proxy Support: Added support for proxies to enable

 the use of proxy servers for network requests. |

#   To-Do List:

- [ ] User-Agent Randomization: Randomly select a user-agent header during requests, which can be achieved by maintaining a list of user-agent headers.
- [ ] Cookie Management: Allow users to pass and manage cookies in requests, which can be achieved using the cookies parameter provided by the requests library.
- [ ] Connection Pool Management: Maintain a connection pool to improve performance, which can be achieved using the Session object provided by the requests library for connection reuse.
- [ ] Custom Timeout Settings: Allow users to set request timeout duration, which can be achieved using the timeout parameter provided by the requests library.
- [ ] Redirection Handling: Add support for handling redirects and provide options to control whether to automatically follow redirects, which can be controlled using the allow_redirects parameter.
- [ ] SSL Certificate Verification: Allow users to control SSL certificate verification, which can be achieved using the verify parameter provided by the requests library.
- [ ] Logging: Add logging functionality to log errors and warnings, which can be achieved using Python's built-in logging module.
- [ ] User Interface Interaction: Provide an interactive interface, which can be implemented using command-line interaction or GUI libraries.
- [ ] Concurrent Request Support: Add support for concurrent requests, which can be achieved using asynchronous libraries such as asyncio and aiohttp.
- [ ] Page Content Parsing: Add functionality for parsing page content, which can be achieved using parsing libraries such as BeautifulSoup and lxml.
- [ ] HTTP/2 Support: Implement support for the HTTP/2 protocol if needed, which can be achieved using libraries that support HTTP/2.
- [ ] Custom Request Headers: Allow users to set custom request headers, which can be achieved using the headers parameter.
- [ ] HTTP Authentication Support: Add support for basic and digest HTTP authentication, which can be achieved using the auth parameter.
- [ ] Data Caching: Provide data caching functionality, which can be implemented using caching libraries or by maintaining a custom caching system.

