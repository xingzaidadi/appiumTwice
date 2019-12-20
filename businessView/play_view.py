from common.common_tools import Common
from appium.webdriver.common.mobileby import By
import logging


class PlayView(Common):
    no_palyaddress = "com.qihoo.livecloud.demo:id/tv_no_play_address"
    live_video = "com.qihoo.livecloud.demo:id/btn_live"
    business_id = "com.qihoo.livecloud.demo:id/et_busuness_id"
    channel_id = "com.qihoo.livecloud.demo:id/et_channel_id"
    sn_num = "com.qihoo.livecloud.demo:id/et_sn"
    soft_decoded = "com.qihoo.livecloud.demo:id/rb_config_decoded_soft"
    have_playaddress = "com.qihoo.livecloud.demo:id/tv_have_play_address"
    url_address = "com.qihoo.livecloud.demo:id/et_url"
    live_startButton = "com.qihoo.livecloud.demo:id/iv_play"

    no_palyaddress_var = (By.ID, no_palyaddress)
    live_video_var = (By.ID, live_video)
    business_id_var = (By.ID, business_id)
    channel_id_var = (By.ID, channel_id)
    sn_num_var = (By.ID, sn_num)
    soft_decoded_var = (By.ID, soft_decoded)
    have_playaddress_var = (By.ID, have_playaddress)
    url_address_var = (By.ID, url_address)
    live_startButton_var = (By.ID, live_startButton)

    def click_line_viode(self):
        self.find_element(*self.live_video_var).click()

    def click_no_playaddr(self):
        self.find_element(*self.no_palyaddress_var).click()

    def input_BusinessID(self,businessID):
        self.find_element(*self.business_id_var).clear()
        self.find_element(*self.business_id_var).send_keys(businessID)

    def input_channelID(self,channelID):
        self.find_element(*self.channel_id_var).clear()
        self.find_element(*self.channel_id_var).send_keys(channelID)

    def input_sn_num(self,sn):
        self.find_element(*self.sn_num_var).clear()
        self.find_element(*self.sn_num_var).send_keys(sn)

    def clicl_soft_decoded(self):
        self.find_element(*self.soft_decoded_var).click()

    def clicl_haveAdrress(self):
        self.find_element(*self.have_playaddress_var).click()

    def input_urladdr(self,url):
        self.find_element(*self.url_address_var).send_keys(url)

    def click_start_livevideo(self):
        self.find_element(*self.live_startButton_var).click()

    #  无地址播放H264视频播放
    def play1_H264_noaddress(self, Bid="demo", cid="live_huajiao_v2", sn=None):
        logging.info('======play1_H264_noaddress=====')
        self.driver.implicitly_wait(10)
        self.click_line_viode()
        self.click_no_playaddr()
        self.input_BusinessID(Bid)
        self.input_channelID(cid)
        self.input_sn_num(sn)
        self.click_start_livevideo()

    #  无地址播放H265视频播放
    def play1_H265_noaddress(self, Bid="demo", cid="live_huajiao_v2", sn=None):
        logging.info('======play1_H265_noaddress=====')
        self.driver.implicitly_wait(10)
        self.click_line_viode()
        self.click_no_playaddr()
        self.input_BusinessID(Bid)
        self.input_channelID(cid)
        self.input_sn_num(sn)
        self.click_start_livevideo()
