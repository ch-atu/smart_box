
# !/usr/bin/env python
# coding:utf-8
__author__ = 'ferraborghini'
from socket import *
import struct


# 将16进制数据当做字节流传递
def dataSwitch(data):
    str1 = ''
    str2 = ''
    while data:
        str1 = data[ 0 : 2 ]
        s = int (str1, 16 )
        str2 += struct.pack( 'B' ,s)
        data = data[2:]
    return str2


if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 21567
    BUFSIZE = 1024
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    while True:
        data = raw_input('>')
        if not data:
            break
        tcpCliSock.send(dataSwitch(data))
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print
        data
    tcpCliSock.close()


# !/usr/bin/env python
# coding:utf-8
from socket import *
from time import ctime

if __name__ == "__main__":
    HOST = ''  # 此处为空代表可以绑定所有有效地址
    PORT = 21567
    BUFSIZE = 1024
    ADDR = (HOST, PORT)
    tcpSerSocket = socket(AF_INET, SOCK_STREAM)
    tcpSerSocket.bind(ADDR)
    tcpSerSocket.listen(5)  # 最多可以有5个连接同时进入
    while True:
        print
        'waiting for connection...'
        tcpCliSock, addr = tcpSerSocket.accept()
        print
        '...connected from:', addr

        while True:
            data = tcpCliSock.recv(BUFSIZE)
            print
            data.encode('hex')
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (ctime(), data))
            # tcpCliSock.close()　　　　　　　　#如果接收完，就断开的话，下次再发送就会报错，书本上有问题
    tcpSerSocket.close()











