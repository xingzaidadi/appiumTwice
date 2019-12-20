from common import appium_driver
import multiprocessing
from tools.AndroidDebugBridge import AndroidDebugBridge as myadb

def muti_phones(port):

    desired_process = []

    # 此处根据手机数量创建进程
    phoneslist = myadb().phonesinfo_list()
    if phoneslist is None:
        return "no phones"
    phone_num = len(phoneslist)
    for i in range(phone_num):

        port1 = port + 2 * i
        pinfo = phoneslist[i]
        desired = multiprocessing.Process(target=appium_driver.appium_desired,
                                          args=(pinfo.platformsversion, pinfo.phonename, pinfo.udid, port1))
        desired_process.append(desired)
    return desired_process


def start_mutli_phones(port):
    phones = muti_phones(port)
    # 启动多设备执行测试
    for desired in phones:
        desired.start()
    for desired in phones:
        desired.join()


if __name__ == '__main__':
    start_mutli_phones(4723)

