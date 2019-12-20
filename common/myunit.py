import unittest
from common import appium_driver
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp====')
        self.driver=appium_driver.appium_desired()

    def tearDown(self):
        logging.info('====tearDown====')
        sleep(5)
        self.driver.close_app()