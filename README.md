
**web_utils.py Library: Providing a Unified Solution for Web Requests**
===============================
[English Documentation](README.md) | [中文文档](README_CN.md)
> **Note:**
>If there is a conflict between the Chinese and English documents, please prioritize the English document.




In the digital age, data has never been more important. Every day, developers, data scientists, and business analysts are striving to retrieve, analyze, and leverage data from the web. However, there is currently a wide variety of web request libraries, each with its unique interface and usage methods. This not only makes learning and switching costly but also introduces complexity and instability into the code.

The birth of the **WebFetcher** library stems from the desire for a unified, efficient, and straightforward solution for web requests. Whether you are using requests, urllib, or Selenium under the hood, **WebFetcher** provides you with a unified and concise interface. This means you can freely switch backend technologies without altering any core code, ensuring code readability and maintainability.

But this is just our first step. We believe that community strength is essential to making this library truly influential and widely used. Whether you are a beginner or an experienced developer, we sincerely invite you to participate in this project. You can contribute not only by submitting code and improving features but also by sharing your usage experience and suggestions to help us. Only through cooperation can **WebFetcher** truly become an essential tool in every developer's toolbox.

If you are passionate about web development and have an unwavering pursuit of innovation and excellence, please join us! Let's work together to create a powerful, flexible, and user-friendly web request library that serves developers worldwide.

`web_utils.py` contains a class named **WebFetcher**, which offers various methods for fetching web content.


import library
--
```
import requests
from urllib import request, parse, error
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
```

The WebFetcher class
------------

### initialization
```
def __init__(self, backend='requests'):
    self.backend = backend
    self.driver = None
 ```

Initialize the WebFetcher class with the backend parameter (default is 'requests').

### request
```
def request(self, method, url, **kwargs):
    ...
```

Send an HTTP request. The supported methods are GET, POST, PUT, and DELETE. You can use 'requests', 'urllib', or 'selenium' as a backend to send requests.

### Selenium Helper Methods


*   **fill_form_by_id**: Fill in form elements by ID.
*   **click_button_by_id**: Click buttons by ID.
*   **scroll_to_bottom**: Scroll to the bottom of the page.
*   **execute_script**: Execute JavaScript scripts.


### close
```
def close(self):
    ...
```

If you're using **Selenium** as a backend, this method will close the **WebDriver** session.

### HTTP Methods

*   **get**: Send a GET request.
*   **post**: Send a POST request.
*   **put**: Send a PUT request.
*   **delete**: Send a DELETE request.

These methods are convenient forms of the **request** method for sending specific HTTP requests.




#### Using the `WebFetcher` Class

### Using `requests` as the Backend

To use the `WebFetcher` class with `requests` as the backend, you can follow these steps:
```
from web_utils import WebFetcher

fetcher = WebFetcher(backend='requests')
response = fetcher.get("https://example.com")
print(response)

```

### Using `urllib` as the Backend

To use the `WebFetcher` class with `urllib` as the backend, you can follow these steps:

```
fetcher = WebFetcher(backend='urllib')
response = fetcher.get("https://example.com")
print(response)
```
### Using `selenium` as the Backend

To use the `WebFetcher` class with `selenium` as the backend, you can follow these steps:

```
fetcher = WebFetcher(backend='selenium')
response = fetcher.get("https://example.com")
print(response)
```
#  Selenium Helper Methods
```
fetcher.scroll_to_bottom()
fetcher.fill_form_by_id("myFormId", "Some Value")
fetcher.click_button_by_id("myButtonId")
script_output = fetcher.execute_script("return document.title;")
print(script_output)

fetcher.close()  # close the `WebDriver` session
```
Note that using Selenium may require additional setup, such as installing the appropriate browser driver.

