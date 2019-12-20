# _*_ coding:utf-8 _*_
import yaml
from appium import webdriver
import time,os
from testcase.test_play import TestPlay

def appium_desired(platformVersion, deviceName, udid, port):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    yaml_path = os.path.join(base_dir, 'config', 'desired_caps.yaml')
    with open(yaml_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        desired_caps['udid'] = udid
        desired_caps['noReset'] = data['noReset']
        desired_caps['unicodeKeyboard'] = data['unicodeKeyboard'] #unicodeKeyboard=True 使用Unicode输入法
        desired_caps['resetKeyboard'] = data['resetKeyboard'] #resetKeyboard=True 测试结束后，重置输入法到原有状态

        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']

        print('start run app...')
        driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)

        driver.implicitly_wait(5)

        TestPlay(driver).H264_noaddress()

    return driver





