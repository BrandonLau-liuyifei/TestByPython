# -*- coding: utf-8 -*-
# @Author : Brandon
from selenium import webdriver


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://ceshiren.com/')

    def teardown(self):
        pass

    # def test_wait(self):
