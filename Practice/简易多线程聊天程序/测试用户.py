#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import socket
import threading

local_addr = ('192.168.3.7', 9080)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(local_addr)


def send_msg(local_ip_port):
    # with open('record.txt', 'a', encoding='utf-8') as f:
    while True:
        msg = input('发送消息：')
        # f.write('她：' + msg + '\n')
        # f.write(f'来自 {local_ip_port[0]} 的 {local_ip_port[1]} 端口：' + msg + '\n')
        # f.write(f'[来自 {local_ip_port[0]} 的 {local_ip_port[1]} 端口]：' + msg + '\n')
        # f.flush()
        sk.sendto(msg.encode('utf-8'), ('192.168.3.7', 9070))
        if msg == 'q':
            break


if __name__ == '__main__':
    send_msg(local_addr)
