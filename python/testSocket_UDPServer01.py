'''
UDP通信测试程序
- 不存在连接，所以server侧不需要调用accept函数，client侧也不需要调用connect函数
- 多次收发,使用recvfrom接收数据， 使用sendto发送数据。
'''

import socket
port=8099
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#从指定的端口，从任何发送者，接收UDP数据
s.bind(('localhost',port))
print('正在等待接入...')
while True:
    #接收一个数据
    recv_data,addr=s.recvfrom(1024)
    data_str = str(recv_data,encoding='utf-8')
    print('Received:',data_str,'from',addr)

    s.sendto(bytes("I have got it !",encoding='utf-8'),addr)
    if data_str == 'exit' or data_str == '' :
        break

s.close()

