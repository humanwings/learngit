'''
TCP客户端 01
-  需要先启动TCP服务器01
-  一发一收
'''

import socket

print("创建socket对象...", end="")
sk = socket.socket()
print("OK")

ip = "127.0.0.1"
port = 8888

print("主动初始化与服务器端的连接  地址：", ip, "端口：", port, " connect()...", end="")
sk.connect((ip, port))  # 主动初始化与服务器端的连接
print("OK Socket is:", sk)

send_data = input("\n输入发送内容：")
sk.sendall(bytes(send_data, encoding="utf8"))
print("内容已发送")

print("\n等待接收信息 recv() ....")
accept_data = sk.recv(1024) # conn.recv()接收客户端的内容，接收到的是bytes类型数据，

accept_data2 = str(accept_data, encoding="utf8")    # str(data,encoding="utf8")用“utf8”进行解码

print("接收内容：", accept_data2)

print("关闭socket...", end="")
sk.close()
print("OK")
