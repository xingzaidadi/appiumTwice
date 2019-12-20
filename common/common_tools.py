#coding:utf-8
from common.base_view import BaseView
import time,os,logging,csv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.common.exceptions import NoSuchElementException


class Common(BaseView):

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def getTime(self):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        return now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file= os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.25)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeRight(self):
        logging.info('swipeRight')
        l = self.get_size()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[1] * 0.75)
        self.swipe(x1, y1, x2, y1, 1000)

    def swipeUp(self):
        logging.info('swipeUp')
        l = self.get_size()
        x1=int(l[0] * 0.5)
        y1=int(l[1] * 0.75)
        y2=int(l[1] * 0.25)
        self.swipe(x1, y1, x1, y2, 1000)

    def swipeDown(self):
        logging.info('swipeUp')
        l = self.get_size()
        x1=int(l[0] * 0.5)
        y1=int(l[1] * 0.25)
        y2=int(l[1] * 0.75)
        self.swipe(x1, y1, x1, y2, 1000)

    def get_csv_data(self,csv_file,line):
        logging.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

    # 获取toast文本
    def find_toast(self, message, timeout, poll_frequency):
        '''可传入部分文本来获取完整文本信息'''
        message1 = "//*[contains(@text=\'{}\')]".format(message)
        element = ""
        try:
            element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located((By.XPATH, message1)))
        except NoSuchElementException:
            logging.info('no such element'+element)

        return element.text
    # 多点滑动，类似操作九宫格
    def multipoint_swipe(self,points):
        try:
            touch_action = TouchAction(self.driver)
            press_xy = points[0]
            touch_action.press(press_xy[0],press_xy[1])
            for i in points[1:]:
                touch_action.move_to(i[0], i[1]).wait(1000)
            touch_action.release().perform()
        except:
            logging.info('zoom-in')


    # 放大地图的操作
    def zoom_in(self):
        try:
            x,y = self.get_size()
            action1 = TouchAction(self.driver)
            action2 = TouchAction(self.driver)
            zoom_action = MultiAction(self.driver)

            action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
            action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()
            logging.info('start zoom-in...')
            zoom_action.add(action1, action2)
            zoom_action.perform()
        except:
            logging.info('zoom-in')

    # 缩小地图的操作
    def zoom_out(self):
        try:
            x, y = self.get_size()
            action1 = TouchAction(self.driver)
            action2 = TouchAction(self.driver)
            zoom_action = MultiAction(self.driver)

            action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000).release()
            action2.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.6, y=y * 0.6).wait(1000).release()

            logging.info('start zoom-out...')
            zoom_action.add(action1, action2)
            zoom_action.perform()
        except:
            logging.info('zoom-in')

    # 等待元素，10秒后未出现则结束寻找
    def waitForElementPresent(self,*loc):
        try:
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_all_elements_located(loc))
        except NoSuchElementException:
            logging.info('no such element')
        else:
            logging.info("find_element")
















