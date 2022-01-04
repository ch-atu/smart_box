import socket
import struct



def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('127.0.0.1', 7890))
        sock.listen(128)
        # req = struct.pack('8B', int('3F', 16), int('20', 16), int('63', 16), int('31', 16), int('0D', 16),
        #                   int('0A', 16), int('0D', 16), int('0A', 16))
        # sock.send(req)
        #
        # time.sleep(1)

        rec = sock.recv(1024)
        rec1 = struct.unpack('6B', rec)
        print(rec1)
        temp = int(chr(rec1[2])) * 100 + int(chr(rec1[3])) * 10 + int(chr(rec1[4]))
        sock.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

