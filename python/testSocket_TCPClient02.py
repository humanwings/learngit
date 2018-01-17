'''
TCP客户端 02
-  需要先启动TCP服务器02
-  进行多次收发，直到客户端发出exit或者空消息
'''

import socket

#客户端创建socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
ip_port = ('127.0.0.1',9999)
#使用connect方法连接服务端，连接失败会报错
#也可以使用connect_ex方法，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回失败编码，例如：10061
client.connect(ip_port)

while True:
    # 从服务端获取数据
    recv_data = client.recv(1024)
    print('接收信息:',str(recv_data,encoding='utf-8'))
    # 客户端发送数据
    s = input('\n发送信息:').strip()
    if len(s) == 0:
        break
    client.send(bytes(s,encoding='utf-8'))
    if s == 'exit':
        break

print("关闭socket...", end="")
client.close()
print("OK")
