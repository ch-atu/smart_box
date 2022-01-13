from gevent import monkey
import gevent
import socket
from datetime import datetime
import sys
import re
import binascii


monkey.patch_all()


class WSGIServer(object):
    """定义一个WSGI服务器的类"""

    def __init__(self, port):

        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 配置地址可重复使用
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 3. 绑定本地信息
        self.server_socket.bind(("127.0.0.1", port))
        # 4. 变为监听套接字
        # 128的含义：指定系统允许暂未 accept 的连接数，超过后将拒绝新连接。未指定则自动设为合理的默认值。
        self.server_socket.listen(128)

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:
            new_socket, new_addr = self.server_socket.accept()
            gevent.spawn(self.deal_with_request, new_socket)  # 创建一个协程准备运行它

    def deal_with_request(self, client_socket):
        """为这个浏览器服务器"""
        while True:
            # 接收数据
            try:
                request = client_socket.recv(1024*1024)
                # print(gevent.getcurrent())
                print('收到的消息是：', request)
                print('时间是：', datetime.now())
            except UnicodeDecodeError as e:
                print('解码时出现错误：', e)
                continue

            # 当浏览器接收完数据后，会自动调用close进行关闭，因此当其关闭时，web也要关闭这个套接字
            if not request:
                client_socket.close()
                break

            # send_data = request
            send_data = response_data(request)
            print('回传的数据是：', send_data)
            client_socket.send(send_data)


def response_data(request):
    # 1.接收上行数据的bytes转成字符串
    str_hex = str(binascii.b2a_hex(request))[2:-1]

    # 2.将上行数据的十六进制字符串转为列表
    list_hex = re.findall(r'.{2}', str_hex)

    # 3.拼接上行数据应答列表
    response_hex_list = list_hex[0:7] + ['c1'] + list_hex[8:10] + ['01', '00']

    # 4.对上行数据应答列表进行十六进制求和
    check_sum_str = hex(sum([int(i, 16) for i in response_hex_list]))[-4:]
    if 'x' in check_sum_str:
        check_sum_str = check_sum_str.replace('x', '0')

    # 5.提取check_sum的高低字节
    check_sum = [check_sum_str[0:2], check_sum_str[2:]]

    # 6.将check_sum插入上行响应数据，低字节在前，高字节在后
    response_hex_list.insert(10, check_sum[1])
    response_hex_list.insert(11, check_sum[0])

    # 7.将上行响应数据列表转为十六进制字符串
    response_hex_str = ''.join(response_hex_list)

    # 8.将上行响应数据列表转为十六进制字符串转为bytes
    response_hex = binascii.a2b_hex(response_hex_str)
    return response_hex


def main():
    """控制web服务器整体"""
    print('服务器启动')
    http_server = WSGIServer(7890)
    http_server.run_forever()


if __name__ == "__main__":
    main()



























