# -*- coding: utf-8 -*-
# @Author : Brandon

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://ceshiren.com/')
        # self.driver.implicitly_wait(3)

    def teardown(self):
        pass

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="按类别分组的所有话题"]').click()
        # sleep(3)
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@title="有新帖子的话题"]')) >= 1
        # WebDriverWait(self.driver,10).until(wait)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@title="有新帖子的话题"]')))
        self.driver.find_element(By.XPATH, '//*[@title="过去一年、一个月、一周或一天中最活跃的话题"]').click()
        print("hello")
