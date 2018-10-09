#!/usr/bin/env python
#--coding: utf8--
import socket
import time

class TimeServer(object):
    def __init__(self, host, port):
        self.addr = (host, port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.addr)
        self.server.listen(1)

    def mainloop(self):
        while True:
            cli_sock, cli_addr = self.server.accept()
            self.handle_child(cli_sock)
            cli_sock.close()
        self.server.close()

    def handle_child(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.rstrip() == '':
                break

            cli_sock.send('[%s] %s' % (time.ctime(), data))


if __name__ == '__main__':
    s = TimeServer('', 21567)
    s.mainloop()
