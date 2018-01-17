'''
TCP服务器02
- server和client 1对N, 在交互期间如果有其他client连接，可以连接成功，但需要等到前一个client中止交互才能继续，无法并行通信。
- 进行多次收发，直到客户端发出exit或者空消息
'''

import socket

#创建一个socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
ip_port = ('127.0.0.1',9999)
#绑定ip和端口号
sock.bind(ip_port)
#设置最大连接数
sock.listen(5)


while True:
    #使用accept方法获取一个客户端连接
    #获取客户端的scoket对象conn和客户端的地址(ip、端口号)address
    conn,address = sock.accept()

    print("\nOK 有客户端连接成功了！")
    print("Socket is：", conn)              # conn是新的socket，用来收发数据
    print("clientAddress is : ",address)       # addr为客户端的端口地址

    
    # 给客户端发信息
    send_data = 'Hello.'
    conn.send(bytes(send_data,encoding='utf-8'))
    while True:
        try:
            # 接收客户端消息
            print("\n等待接收信息 recv() ....")
            recv_data = conn.recv(1024)
            recv_data_str = str(recv_data,encoding='utf-8')
            #检测客户端发出退出指令，关闭连接
            if recv_data_str == 'exit' or recv_data_str == '' :
                print("收到客户端的终止请求")
                break
            else:
                print("接收内容：", recv_data_str, "    客户地址：", address)
            s = input('Server:').strip()
            if len(s) == 0:
                break
            s = "I have got it!"
            conn.send(bytes(s,encoding='utf-8'))
        except Exception as e:
            break

    # 关闭客户端的socket连接
    print("关闭本次连接...", end="")
    conn.close()
    print("OK")
    s = input('回车继续:').strip()
    if len(s) != 0:
        break

sock.close()
print("\n测试结束！")
