import socket, os,logging


# 检查端口号是否被占用
# 释放端口

def check_port(ip, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sk.connect((ip, port))
        sk.shutdown(2)
    except OSError as msg:
        logging.info('port %s is available! ' % port)
        # print(msg)
        return True
    else:
        logging.error('port %s already be in use !' % port)
        return False


def release_port(port):
    # 释放指定的端口

    # 查找对应端口的pid
    cmd_find = 'netstat -aon | findstr %s' % port
    # print(cmd_find)

    # 返回命令执行后的结果
    result = os.popen(cmd_find).read()
    # print(result)

    if str(port) and 'LISTENING' in result:
        # 获取端口对应的pid进程
        i = result.index('LISTENING')
        start = i + len('LISTENING') + 7
        end = result.index('\n')
        pid = result[start:end]

        # 关闭被占用端口的pid
        cmd_kill = 'taskkill -f -pid %s' % pid
        # print(cmd_kill)
        os.popen(cmd_kill)
        logging.info("由于技术原因，请2分钟后再次使用该端口。或者自行使用netstat命令关闭")

    else:
        logging.error('port %s is available !' % port)


if __name__ == '__main__':

    if not check_port("127.0.0.1", 4723):
        release_port(4723)

