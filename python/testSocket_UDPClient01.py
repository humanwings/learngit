'''
UDP通信测试程序
- 不存在连接，所以server侧不需要调用accept函数，client侧也不需要调用connect函数
- 多次收发,使用recvfrom接收数据， 使用sendto发送数据。
'''

import socket

port=8099
host='localhost'
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

info = input('\n发送信息:').strip()

s.sendto(bytes(info,encoding='utf-8'),(host,port))

recv_data,addr=s.recvfrom(1024)
data_str = str(recv_data,encoding='utf-8')
print('Received:',data_str,'from',addr)

