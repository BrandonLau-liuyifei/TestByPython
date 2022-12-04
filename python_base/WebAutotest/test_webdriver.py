# -*- coding: utf-8 -*-
# @Author : Brandon
from selenium import webdriver


def test_webdriver():
    driver = webdriver.Chrome()
    driver.get("https://baidu.com")
