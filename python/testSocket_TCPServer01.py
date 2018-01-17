'''
TCP服务器01
- server和client 1对1, 在交互期间如果有其他client连接，可以连接成功，但是无法交互。
- 只进行一次收发
'''

import socket  # 导入socket模块

print("创建socket对象...", end="")
sk = socket.socket()  # 缺省family=AF_INET(服务器之间网络通信), type=SOCK_STREAM(流式socket，用于TCP)
print("OK")

ip = "127.0.0.1"
port = 8888

print("绑定地址：", ip, "端口：", port, "...", end="")
sk.bind((ip, port))  # AF_INET 的address family使用一个(host, port)的tuple来作为地址格式。
print("OK")

print("开始TCP监听(最多可有5个客户端进行排队)...", end="")
sk.listen(5)  # 设置监听，
print("OK")

print("Socket is：", sk)
print("阻塞式等待连接的到来（被动接受TCP客户端连接,此时服务器侧的socket并没有打开）...")
conn, addr = sk.accept()  # 阻塞状态，被动等待客户端的连接
print("\nOK 有客户端连接成功了！")

print("Socket is：", conn)              # conn是新的socket，用来收发数据
print("clientAddress is : ",addr)       # addr为客户端的端口地址

print("\n等待接收信息 recv() ....")
accept_data = conn.recv(1024)  # conn.recv()接收客户端的内容，接收到的是bytes类型数据，

accept_data2 = str(accept_data, encoding="utf8")  # str(data,encoding="utf8")用“utf8”进行解码

print("接收内容：", accept_data2, "    客户地址：", addr)

send_data = input("\n输入发送内容：")

conn.sendall(bytes(send_data, encoding="utf8"))  # 发送内容必须为bytes类型数据，bytes(data, encoding="utf8")用“utf8”格式进行编码

print("内容已发送")

print("关闭socket...", end="")
conn.close()
print("OK")
