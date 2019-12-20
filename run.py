from common import  multi_devices_sync,muti_appium_server_sync

# 多进程启动多手机，在多手机上执行自动化
if __name__ == '__main__':
    muti_appium_server_sync.appium_servers(4723)
    multi_devices_sync.start_mutli_phones(4723)