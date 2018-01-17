'''
TCP服务器03
- server和client 1对N, 支持并行通信。
- 进行多次收发，直到客户端发出exit或者空消息
'''

import socket, threading, time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


#创建一个socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
ip_port = ('127.0.0.1',9999)
#绑定ip和端口号
sock.bind(ip_port)
#设置最大连接数
sock.listen(5)

print("开始TCP监听(最多可有5个客户端进行排队)...\n")

while True:
    # 接受一个新连接:
    conn, addr = sock.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(conn, addr))
    t.start()


