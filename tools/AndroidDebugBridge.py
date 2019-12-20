# python module for interacting with adb
import os
from tools.phoneinfo import PhoneInfo


class AndroidDebugBridge(object):
    def call_adb(self, command):
        command_result = ''
        command_text = 'adb %s' % command
        # print(command_text)
        results = os.popen(command_text, "r")
        while 1:
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result

    # check for any fastboot device
    def fastboot(self, device_id):
        pass

    # 检查设备
    def attached_devices(self):
        result = self.call_adb("devices")
        devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
        return [device for device in devices if len(device) > 2]


    # 状态
    def get_state(self):
        result = self.call_adb("get-state")
        result = result.strip(' \t\n\r')
        return result or None

    # 重启
    def reboot(self, option):
        command = "reboot"
        if len(option) > 7 and option in ("bootloader", "recovery",):
            command = "%s %s" % (command, option.strip())
        self.call_adb(command)

    # 将电脑文件拷贝到手机里面
    def push(self, local, remote):
        result = self.call_adb("push %s %s" % (local, remote))
        return result

    # 拉数据到本地
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s" % (remote, local))
        return result

    # 同步更新 很少用此命名
    def sync(self, directory, **kwargs):
        command = "sync %s" % directory
        if 'list' in kwargs:
            command += " -l"
            result = self.call_adb(command)
            return result

    # 打开指定app
    def open_app(self, packagename, activity, devices):
        result = self.call_adb("-s " + devices + " shell am start -n %s/%s" % (packagename, activity))
        check = result.partition('\n')[2].replace('\n', '').split('\t ')
        if check[0].find("Error") >= 1:
            return False
        else:
            return True

    # 根据包名得到进程id
    def get_app_pid(self, pkg_name):
        string = self.call_adb("shell ps | grep " + pkg_name)
        # print(string)
        if string == '':
            return "the process doesn't exist."
        result = string.split(" ")
        # print(result[4])
        return result[4]


    # 获取所有在线手机的序列号
    def get_devices_udid(self):
        result = os.popen("adb devices")
        lines = result.readlines()
        lnew = lines[1:-1]
        # print(lnew)
        udidlist = []
        for i in range(len(lnew)):
            udid = lnew[i].strip("\n").split("\t")[0]
            # print(udid)
            udidlist.append(udid)
        # print(udidlist)
        return udidlist

    # 获取手机系统版本号
    def get_platforms_version(self):
        pv_list = []
        devices_udid = self.get_devices_udid()
        for i in range(len(devices_udid)):

            cmd = "-s "+devices_udid[i]+" shell getprop ro.build.version.release"
            pversion = self.call_adb(cmd).strip("\n")
            pv_list.append(pversion)
        return pv_list

    # 获取手机的名字
    def get_phonename(self):
        pname_list = []
        devices_udid = self.get_devices_udid()
        for i in range(len(devices_udid)):
            cmd = "-s " + devices_udid[i] + " shell getprop ro.product.model"
            pversion = self.call_adb(cmd).strip("\n")
            pname_list.append(pversion)
        return pname_list

    # 封装数据udid,platformsversion,phonename到对象，并组成list.
    # 多手机时使用。
    def phonesinfo_list(self):
        phonesinfo_list = []

        pv = self.get_platforms_version()
        udid = self.get_devices_udid()
        pname = self.get_phonename()

        for i in range(len(udid)):
            pinfo = PhoneInfo(udid[i], pv[i], pname[i])
            phonesinfo_list.append(pinfo)

        return phonesinfo_list

    # 获取当前appiumserver的pid 需要端口
    def appium_server_pid(self):
        pass


if __name__ == '__main__':

    adb = AndroidDebugBridge()
    pv = adb.get_platforms_version()
    udid = adb.get_devices_udid()
    pname = adb.get_phonename()
    phonesinfo_list =[]
    for i in range(len(udid)):
        pinfo = PhoneInfo(udid[i],pv[i],pname[i])
        phonesinfo_list.append(pinfo)

    print(phonesinfo_list[0].phonename)

