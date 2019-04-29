#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by charles on 2019-04-29
# Function: 

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    install_requires=["requests>=2.18.4", "beautifulsoup4>=4.6.0", "lxml>=4.1.0"],
    name="baidusearch",
    version="1.0.1",
    author="Wu Charles",
    maintainer='Wu Charles',
    author_email="wcadaydayup@163.com",
    description="Baidu Search unofficial API for Python with no external dependencies",
    keywords="search-api baidu python",
    url="https://github.com/wcadaydayup/python-baidusearch",
    packages=find_packages(),
    platforms=["all"],
    exclude_package_data={
        '': ['config.json', '__pycache__/*']
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    include_package_data=True,  # needed for MANIFEST

    entry_points={
        'console_scripts': [
            'baidusearch = baidusearch.baidusearch:run',
        ],
    }
)
