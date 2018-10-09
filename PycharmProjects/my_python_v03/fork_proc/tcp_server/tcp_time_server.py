#!/usr/bin/env python3
#--*--coding: utf8--*--
import socket
import time

class TcpTimeServer():
    def __init__(self, host, port):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(2)

    def handle_child(self, cli_sock):
        while True:
            data = str(cli_sock.recv(1024), encoding='utf8')
            if not data.strip():
                break
            data = '[%s]: %s' % (time.strftime('%H:%M:%S'), data)
            cli_sock.sendall(bytes(data, encoding='utf8'))
        cli_sock.close()

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                break
            self.handle_child(cli_sock)
            cli_sock.close()
        self.serv.close()

if __name__ == '__main__':
    s = TcpTimeServer('', 12345)
    s.mainloop()