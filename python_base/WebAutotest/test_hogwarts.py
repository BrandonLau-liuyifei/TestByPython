# -*- coding: utf-8 -*-
# @Author : Brandon
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get('https://testerhome.com')
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        self.driver.find_element(By.LINK_TEXT, 'Jenkins 中文社区').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic-27128 .title > a').click()
        # 中间没有等待，第二个元素没能及时加载处来，导致报错，可以在setup等待机制
