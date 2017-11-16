# -*- coding: utf-8 -*-
# @Time     : 2017/11/16 23:44
# @Author   : zhaoshun
# @Email    : tmby1314@163.com

"""
"""
import socket

s = socket.socket()
s.connect(('www.baidu.com', 80))
print("We are connected to %s:%d" % s.getpeername())

