# -*- coding: utf-8 -*-
# @Time     : 2017/11/16 23:44
# @Author   : zhaoshun
# @Email    : tmby1314@163.com

"""
"""
# import  socket
#
# s = socket.socket()
# s.connect(('www.baidu.com', 80))
# print("We are connected to %s:%d" % s.getpeername())


import socket

import time

s = socket.socket()
s.setblocking(0)

try:
    s.connect(('www.google.com', 80))
except socket.error as e:
    print(str(e))
    i = 0
    while True:
        try:
            print("We are connected to %s:%d" % s.getpeername())
            time.sleep(3)
            break
        except:
            print("Let's do some math while waiting: %d" % i)
            i += 1
else:
    print("We are connected to %s:%d" % s.getpeername())

finally:
    print ("We are connected end")
