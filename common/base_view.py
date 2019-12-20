#coding:utf-8

import logging
from selenium.common.exceptions import NoSuchElementException


class BaseView(object):

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        element = "_".join(loc)
        try:
            self.driver.find_element(*loc)
        except NoSuchElementException:
            logging.info('no such element：'+element)
        else:
            logging.info("find_element："+element)

    def find_elements(self,*loc):
        element = "_".join(loc)
        try:
            self.driver.find_elements(*loc)
        except NoSuchElementException:
            logging.info('no such element：' + element)
        else:
            logging.info("find_element：" + element)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def back(self):
        self.driver.back()

