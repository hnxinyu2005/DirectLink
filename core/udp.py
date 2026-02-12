# core/udp.py
# UDP 核心通信模块

import socket
from utils.config import UDP_PORT, UDP_BUFFER_SIZE

def create_udp_socket():
    """
    创建UDP套接字并绑定端口，让程序能接收或发送UDP消息
    """
    # IPV4, UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(("0.0.0.0", UDP_PORT)) # 所有网卡能访问

    print(f"[UDP] 已启动，监听端口：{UDP_PORT}")
    return udp_socket

def udp_send(udp_socket, target_ip, target_port, data):
    """
    向目标 IP:端口 发送字符串信息
    """
    # 把字符串转换成字节发送
    udp_socket.sendto(data.encode("utf-8"), (target_ip, target_port))
    print(f"[UDP] 发送给 {target_ip}:{target_port} -> {data}")

def udp_receive(udp_socket):
    """
    等待msg
    """
    data, addr = udp_socket.recvfrom(UDP_BUFFER_SIZE)
    msg = data.decode("utf-8")
    print(f"[UDP] 收到自 {addr[0]}:{addr[1]} 的消息 -> {msg}")
    return msg, addr