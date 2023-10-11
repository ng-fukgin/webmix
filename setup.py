from setuptools import setup, find_packages

setup(
    name='webmix',
    version='0.0.1',
    author='wfj',
    author_email='wfj.0000@gmail.com',
    description='一组实用程序，用于网页抓取和自动化，支持多种后端：requests、urllib和selenium。',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ng-fukgin/webutils',
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
    keywords='webutils, 网页抓取, 自动化, requests, urllib, selenium',
    python_requires='>=3.7',
    install_requires=[
        'requests',
        'selenium',
        'webdriver_manager',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/ng-fukgin/webutils/issues',
        'Documentation': 'https://github.com/ng-fukgin/webutils/wiki',
        'Source Code': 'https://github.com/ng-fukgin/webutils',
    },
    license='MIT',
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)