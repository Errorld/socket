import socket
import time

print('building socket')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('connecting socket')
s.connect(('127.0.0.1', 7778))

t0 = time.time()
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Michael', b'Michael', ]:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
t1 = time.time()
print(t1 - t0)
input()
s.send(b'exit')
# s.close
