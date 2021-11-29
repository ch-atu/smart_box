from gevent import monkey
import gevent
import socket
import sys
import re

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
                request = client_socket.recv(1024*1024).decode('gbk')
                # print(gevent.getcurrent())
                print('收到的消息是：', request)
            except UnicodeDecodeError as e:
                print('超出最大字节数：', e)
                request = False

            # 当浏览器接收完数据后，会自动调用close进行关闭，因此当其关闭时，web也要关闭这个套接字
            if not request:
                client_socket.close()
                break

            send_data = 'hello world!!!'
            client_socket.send(send_data.encode('gbk'))


def main():
    """控制web服务器整体"""
    print('服务器启动')
    http_server = WSGIServer(7890)
    http_server.run_forever()


if __name__ == "__main__":
    main()




























