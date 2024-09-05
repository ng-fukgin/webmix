import requests
import http.client
from urllib import request, parse, error
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import aiohttp
import asyncio
import random


class WebFetcher:
    SUPPORTED_METHODS = ['GET', 'POST', 'PUT', 'DELETE']

    def __init__(self, backend='requests', loop=None):
        self.backend = backend
        self.driver = None
        self.loop = loop if loop else asyncio.get_event_loop()

    def request(self, method, url, **kwargs):
        if method.upper() not in self.SUPPORTED_METHODS:
            raise ValueError(f"Unsupported HTTP method: {method}")

        try:
            if self.backend == 'requests':
                if 'proxy' in kwargs:
                    proxies = {'http': kwargs['proxy'], 'https': kwargs['proxy']}
                    kwargs.pop('proxy')
                    kwargs['proxies'] = proxies
                return self._request_with_requests(method, url, **kwargs)

            elif self.backend == 'urllib':
                if 'proxy' in kwargs:
                    proxy_handler = request.ProxyHandler({
                        'http': kwargs['proxy'],
                        'https': kwargs['proxy']
                    })
                    opener = request.build_opener(proxy_handler)
                    request.install_opener(opener)
                return self._request_with_urllib(method, url, **kwargs)

            elif self.backend == 'selenium':
                if 'proxy' in kwargs:
                    raise ValueError("Selenium does not support proxies directly.")
                if method.upper() != 'GET':
                    raise ValueError("Selenium only supports GET method.")
                return self._get_with_selenium(url)

            elif self.backend == 'http.client':
                if 'proxy' in kwargs:
                    raise ValueError("Proxy support for http.client is not implemented.")
                return self._request_with_http_client(method, url, **kwargs)

            elif self.backend == 'aiohttp':
                # aiohttp must be called asynchronously
                if 'proxy' in kwargs:
                    kwargs['proxy'] = kwargs.pop('proxy')
                return self.loop.run_until_complete(self._request_with_aiohttp(method, url, **kwargs))
            else:
                raise ValueError("Unsupported backend!")
        except Exception as e:
            print(f"Error encountered: {e}")
            return None


    
    def find_element_by_id(self, element_id):
        """Find element by ID using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            return self.driver.find_element(By.ID, element_id)
        except WebDriverException as e:
            raise Exception(f"Failed to find element by ID using selenium: {e}")
        
        
    def find_element_by_name(self, element_name):
        """Find element by name using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            return self.driver.find_element(By.NAME, element_name)
        except WebDriverException as e:
            raise Exception(f"Failed to find element by name using selenium: {e}")

    def find_element_by_xpath(self, xpath):
        """Find element by XPath using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except WebDriverException as e:
            raise Exception(f"Failed to find element by XPath using selenium: {e}")

    def wait_for_element_visibility(self, element, timeout=10):
        """Wait for element visibility using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of(element))
        except WebDriverException as e:
            raise Exception(f"Failed to wait for element visibility using selenium: {e}")

    def switch_to_frame(self, frame_reference):
        """Switch to iframe or frame using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.frame(frame_reference)
        except WebDriverException as e:
            raise Exception(f"Failed to switch to frame using selenium: {e}")

    def switch_to_default_content(self):
        """Switch back to default content using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.default_content()
        except WebDriverException as e:
            raise Exception(f"Failed to switch to default content using selenium: {e}")

    def switch_to_window(self, window_handle):
        """Switch to a different browser window using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.window(window_handle)
        except WebDriverException as e:
            raise Exception(f"Failed to switch to window using selenium: {e}")

    def accept_alert(self):
        """Accept alert using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.alert.accept()
        except WebDriverException as e:
            raise Exception(f"Failed to accept alert using selenium: {e}")

    def dismiss_alert(self):
        """Dismiss alert using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.switch_to.alert.dismiss()
        except WebDriverException as e:
            raise Exception(f"Failed to dismiss alert using selenium: {e}")

    def maximize_window(self):
        """Maximize the browser window using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.maximize_window()
        except WebDriverException as e:
            raise Exception(f"Failed to maximize window using selenium: {e}")

    def set_window_size(self, width, height):
        """Set the browser window size using Selenium"""
        if not self.driver:
            raise Exception("Driver not initialized or Selenium not set as backend.")
        try:
            self.driver.set_window_size(width, height)
        except WebDriverException as e:
            raise Exception(f"Failed to set window size using selenium: {e}")

    # Backend-specific request methods
    def _request_with_requests(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()  # 检查 HTTP 状态码

            # 根据响应的 Content-Type 返回相应格式
            content_type = response.headers.get('Content-Type', '').lower()

            return response

        except requests.RequestException as e:
            raise Exception(f"Failed to {method} using requests: {e}")


    def _request_with_requests(self, method, url, **kwargs):
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()  # 检查 HTTP 状态码
            return response
        except requests.RequestException as e:
            raise Exception(f"Failed to {method} using requests: {e}")

    def _request_with_urllib(self, method, url, **kwargs):
        headers = {'User-Agent': self.get_random_user_agent()}

        data = kwargs.get('data')
        if method == 'GET' and 'params' in kwargs:
            url += '?' + parse.urlencode(kwargs['params'])
        if method in ['POST', 'PUT'] and data:
            data = parse.urlencode(data).encode('utf-8')

        req = request.Request(url, data=data, headers=headers, method=method)

        try:
            with request.urlopen(req) as response:
                content_type = response.headers.get('Content-Type', '').lower()

                return response

        except error.URLError as e:
            raise Exception(f"Failed to {method} using urllib: {e}")

    def _request_with_http_client(self, method, url, **kwargs):
        try:
            connection = http.client.HTTPSConnection(url)
            connection.request(method, url, **kwargs)
            response = connection.getresponse()
            return response  # Return full response object
        except Exception as e:
            raise Exception(f"Failed to {method} using http.client: {e}")

    async def _request_with_aiohttp(self, method, url, **kwargs):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.request(method, url, **kwargs) as response:
                    content_type = response.headers.get('Content-Type', '').lower()

                    return await response
        except Exception as e:
            raise Exception(f"Failed to {method} using aiohttp: {e}")

    def _get_with_selenium(self, url):
        try:
            if not self.driver:
                # Use webdriver_manager to automatically manage the Chrome driver
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')  # Run Chrome in headless mode
                self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            self.driver.get(url)
            return self.driver.page_source
        except WebDriverException as e:
            raise Exception(f"Failed to fetch using selenium: {e}")

    def close(self):
        """Close the Selenium driver if initialized"""
        if self.driver:
            self.driver.quit()

    # Convenience methods for HTTP methods
    def get(self, url, **kwargs):
        if self.backend == 'aiohttp':
            raise RuntimeError("Use async method for aiohttp")
        return self.request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        if self.backend == 'aiohttp':
            raise RuntimeError("Use async method for aiohttp")
        return self.request('POST', url, **kwargs)

    def put(self, url, **kwargs):
        if self.backend == 'aiohttp':
            raise RuntimeError("Use async method for aiohttp")
        return self.request('PUT', url, **kwargs)

    def delete(self, url, **kwargs):
        if self.backend == 'aiohttp':
            raise RuntimeError("Use async method for aiohttp")
        return self.request('DELETE', url, **kwargs)
    def get_random_user_agent(self):
        """Return a random user agent string"""
        USER_AGENTS = [
            # Chrome on Windows
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",

            # Chrome on macOS
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",

            # Chrome on Linux
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",

            # Firefox on Windows
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:90.0) Gecko/20100101 Firefox/90.0",

            # Firefox on macOS
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:89.0) Gecko/20100101 Firefox/89.0",

            # Firefox on Linux
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
            "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",

            # Safari on macOS
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",

            # Safari on iOS
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",

            # Edge on Windows
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77",

            # Android
            "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",

            # More user agents can be added here for wider browser/platform support
        ]
        return random.choice(USER_AGENTS)

