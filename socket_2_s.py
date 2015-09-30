import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcom')
    while True:
        data = sock.recv(1024)
        time.sleep(0.1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 7778,))
s.listen(5)
print('Waiting for connection...')
while True:
    # print(s.accept())
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
