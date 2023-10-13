# web_utils.py

import requests
from urllib import request, parse, error
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import http.client
import aiohttp
import aiohttp
import asyncio




class WebFetcher:
    SUPPORTED_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, backend='requests', loop=None):
            self.backend = backend
            self.driver = None
            self.loop = loop if loop else asyncio.get_event_loop()

    async def request(self, method, url, **kwargs):
        if method.upper() not in self.SUPPORTED_METHODS:
            raise ValueError(f"Unsupported HTTP method: {method}")

        try:
            if self.backend == 'requests':
                return await self.loop.run_in_executor(None, lambda: self._request_with_requests(method, url, **kwargs))
            elif self.backend == 'urllib':
                return await self.loop.run_in_executor(None, lambda: self._request_with_urllib(method, url, **kwargs))
            elif self.backend == 'selenium':
                if method.upper() != 'GET':
                    raise ValueError("Selenium only supports GET method.")
                return self._get_with_selenium(url)
            elif self.backend == 'http.client':
                return await self.loop.run_in_executor(None, lambda: self._request_with_http_client(method, url, **kwargs))
            elif self.backend == 'aiohttp':
                return await self._request_with_aiohttp(method, url, **kwargs)
            else:
                raise ValueError("Unsupported backend!")
        except Exception as e:
            print(f"Error encountered: {e}")
            return None

        
    def find_element_by_id(self, element_id):
        """通过ID查找元素 (Find element by ID)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            return self.driver.find_element(By.ID, element_id)
        except WebDriverException as e:
            raise Exception(f"Failed to find element by ID using selenium: {e}")

    def find_element_by_name(self, element_name):
        """通过名称查找元素 (Find element by name)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            return self.driver.find_element(By.NAME, element_name)
        except WebDriverException as e:
            raise Exception(f"Failed to find element by name using selenium: {e}")

    def find_element_by_xpath(self, xpath):
        """通过XPath查找元素 (Find element by XPath)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except WebDriverException as e:
            raise Exception(f"Failed to find element by XPath using selenium: {e}")

    def wait_for_element_visibility(self, element, timeout=10):
        """等待元素可见 (Wait for element visibility)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of(element))
        except WebDriverException as e:
            raise Exception(f"Failed to wait for element visibility using selenium: {e}")

    def switch_to_frame(self, frame_reference):
        """切换到iframe或frame (Switch to iframe or frame)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.frame(frame_reference)
        except WebDriverException as e:
            raise Exception(f"Failed to switch to frame using selenium: {e}")

    def switch_to_default_content(self):
        """切回到默认内容 (Switch back to default content)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.default_content()
        except WebDriverException as e:
            raise Exception(f"Failed to switch to default content using selenium: {e}")

    def switch_to_window(self, window_handle):
        """切换到不同的浏览器窗口 (Switch to a different browser window)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.window(window_handle)
        except WebDriverException as e:
            raise Exception(f"Failed to switch to window using selenium: {e}")

    def accept_alert(self):
        """接受警告框 (Accept alert)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.alert.accept()
        except WebDriverException as e:
            raise Exception(f"Failed to accept alert using selenium: {e}")

    def dismiss_alert(self):
        """取消警告框 (Dismiss alert)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.alert.dismiss()
        except WebDriverException as e:
            raise Exception(f"Failed to dismiss alert using selenium: {e}")

    def maximize_window(self):
        """最大化浏览器窗口 (Maximize the browser window)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.maximize_window()
        except WebDriverException as e:
            raise Exception(f"Failed to maximize window using selenium: {e}")

    def set_window_size(self, width, height):
        """设置浏览器窗口大小 (Set the browser window size)"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.set_window_size(width, height)
        except WebDriverException as e:
            raise Exception(f"Failed to set window size using selenium: {e}")
        
    

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
        
        
    def _request_with_http_client(self, method, url, **kwargs):
        try:
            connection = http.client.HTTPSConnection(url)  # 或者使用HTTPConnection，具体取决于您的需求
            connection.request(method, url, **kwargs)
            response = connection.getresponse()
            return response.read().decode('utf-8')
        except Exception as e:
            raise Exception(f"Failed to {method} using http.client: {e}")



    async def _request_with_aiohttp(self, method, url, **kwargs):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.request(method, url, **kwargs) as response:
                    return await response.text()
        except Exception as e:
            raise Exception(f"Failed to {method} using aiohttp: {e}")


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
