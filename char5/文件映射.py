#coding:utf8

f = open('demo.txt','w',buffering=2048)
#buffering = n, 全缓冲
#buffering = 1, 行缓冲
#buffering = 0, 无缓冲
#

f.write('+'*2048)

import map
f = open('demo.bin','r+b')
f.fileno()
mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)
m[0] = '\x88'
m[4:8] = '\xff'*4
