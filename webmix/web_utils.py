# web_utils.py

import requests
from urllib import request, parse, error
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

class WebFetcher:
    SUPPORTED_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, backend='requests'):
        self.backend = backend
        self.driver = None

    def request(self, method, url, **kwargs):
        if method.upper() not in self.SUPPORTED_METHODS:
            raise ValueError(f"Unsupported HTTP method: {method}")

        try:
            if self.backend == 'requests':
                return self._request_with_requests(method, url, **kwargs)
            elif self.backend == 'urllib':
                return self._request_with_urllib(method, url, **kwargs)
            elif self.backend == 'selenium':
                if method.upper() != 'GET':
                    raise ValueError("Selenium only supports GET method.")
                return self._get_with_selenium(url)
            else:
                raise ValueError("Unsupported backend!")
        except Exception as e:
            print(f"Error encountered: {e}")
            return None
        
    def fill_form_by_id(self, element_id, value):
        """填写具有特定ID的表单元素"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            element = self.driver.find_element_by_id(element_id)
            element.clear()
            element.send_keys(value)
        except WebDriverException as e:
            raise Exception(f"Failed to fill form by ID using selenium: {e}")

    def click_button_by_id(self, button_id):
        """点击具有特定ID的按钮"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            button = self.driver.find_element_by_id(button_id)
            button.click()
        except WebDriverException as e:
            raise Exception(f"Failed to click button by ID using selenium: {e}")

    def scroll_to_bottom(self):
        """滚动到页面底部"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except WebDriverException as e:
            raise Exception(f"Failed to scroll using selenium: {e}")

    def execute_script(self, script):
        """执行JavaScript脚本"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            return self.driver.execute_script(script)
        except WebDriverException as e:
            raise Exception(f"Failed to execute script using selenium: {e}")
        
        
    

    def _request_with_requests(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise Exception(f"Failed to {method} using requests: {e}")

    def _request_with_urllib(self, method, url, **kwargs):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        data = kwargs.get('data')
        if method == 'GET' and 'params' in kwargs:
            url += '?' + parse.urlencode(kwargs['params'])
        if method in ['POST', 'PUT'] and data:
            data = parse.urlencode(data).encode('utf-8')

        req = request.Request(url, data=data, headers=headers, method=method)

        try:
            with request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except error.URLError as e:
            raise Exception(f"Failed to {method} using urllib: {e}")

    def _get_with_selenium(self, url):
        try:
            if not self.driver:
                # 使用 webdriver_manager 自动下载并缓存驱动器
                self.driver = webdriver.Chrome(executable_path=ChromeDriverManager(cache_valid_range=365).install())
            self.driver.get(url)
            return self.driver.page_source
        except WebDriverException as e:
            raise Exception(f"Failed to fetch using selenium: {e}")

    def close(self):
        if self.driver:
            self.driver.quit()

    # Convenience methods for HTTP methods
    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)

    def put(self, url, **kwargs):
        return self.request('PUT', url, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)
