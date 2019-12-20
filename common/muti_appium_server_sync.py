import subprocess, multiprocessing
import time
from tools.AndroidDebugBridge import AndroidDebugBridge as myadb
from tools import checkport


def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'appium -a ' + host + ' -p ' + str(port) + ' --bootstrap-port ' + str(bootstrap_port)

    print('%s at %s' % (cmd, time.ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open('./' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


# 多进程启动appium服务
def appium_servers(port):

    appium_process = []

    phoneslist = myadb().phonesinfo_list()

    phone_num = len(phoneslist)
    for i in range(phone_num):
        ip = '127.0.0.1'  # 此处先写死，后期可改为指定ip，注入即可。
        port1 = port + 2 * i
        if checkport.check_port(ip, port1):
            appium = multiprocessing.Process(target=appium_start, args=(ip, port1))
            appium_process.append(appium)
        else:
            checkport.release_port(port1)

    return appium_process


def start_appium_server(port):
    # 并发启动appium服务
    servers = appium_servers(port)
    for appium in servers:
        appium.start()
    for appium in servers:
        appium.join()


if __name__ == '__main__':
    start_appium_server(4723)
