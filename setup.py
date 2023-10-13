from setuptools import setup, find_packages

setup(
    name='webmix',
    version='0.0.5',
    author='wfj',
    author_email='wfj.0000@gmail.com',
    description='A set of utilities for web scraping and automation, supporting multiple backends: requests, urllib, and selenium.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ng-fukgin/webmix',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    keywords='webmix, 网页抓取, 自动化, requests, urllib, selenium, web scraping, automation ',
    python_requires='>=3.7',
    install_requires=[
        'requests>=2.0.0,<=3.0.0',  # 版本范围示例
        'selenium==3.141.0',
        'webdriver_manager>=1.0.0,<=2.0.0',
        'aiohttp>=3.0.0,<=4.0.0',
        'asyncio>=3.0.0,<=4.0.0',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/ng-fukgin/webmix/issues',
        'Documentation': 'https://github.com/ng-fukgin/webmix/wiki',
        'Source Code': 'https://github.com/ng-fukgin/webmix',
    },
    license='MIT',
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
