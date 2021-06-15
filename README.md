# selenium_youtube_chrome

![PyPI - package version](https://img.shields.io/pypi/v/selenium_youtube_chrome?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/selenium_youtube_chrome?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/selenium_youtube_chrome?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/selenium_youtube_chrome?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/selenium_youtube_chrome?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/selenium_youtube_chrome?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/selenium_youtube_chrome?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/selenium_youtube_chrome?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/selenium_youtube_chrome?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/selenium_youtube_chrome?label=repo%20license&style=flat-square)

## Description

Youtube with selenium chrome

## Install

~~~~bash
pip install selenium_youtube_chrome
# or
pip3 install selenium_youtube_chrome
~~~~

## Usage

~~~~python
from selenium_youtube_chrome import Youtube

youtube = Youtube()
upload_result = youtube.upload('path_to_video', 'title', 'description', ['tag1', 'tag2'])
~~~~

## Dependencies

[kproxy](https://pypi.org/project/kproxy), [selenium-chrome](https://pypi.org/project/selenium-chrome), [selenium-youtube](https://pypi.org/project/selenium-youtube)