import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('sekai.top', 80,))

s.send(b'GET / HTTP/1.1\r\nHost: sekai.top\r\nConnection: colse\r\n\r\n')

buffer = []
count = 0
while True:
    d = s.recv(1024)
    if d:
        count += 1
        if count % 10 == 0:
            print(count)
        buffer.append(d)
    else:
        print('breaking')
        break

print('\n%d\n' % count)
print('\nsaving buffer\n')
data = b''.join(buffer)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('sina.html', 'wb') as f:
    print('\nwriting file\n')
    f.write(html)
