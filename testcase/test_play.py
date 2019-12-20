from common.myunit import StartEnd
from businessView.play_view import PlayView

import logging

class TestPlay(StartEnd):

    def H264_noaddress(self):
        logging.info('======H264_noaddress=====')
        play_view = PlayView()
        play_view.play1_H264_noaddress()

    def H265_noaddress(self):
        logging.info('======H265_noaddress=====')
        play_view = PlayView()
        play_view.play1_H265_noaddress()

