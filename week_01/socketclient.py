import socket

HOST = '192.168.1.86'
PORT = 60080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'www.douban.com')
    data = s.recv(1024)
print('received', repr(data))