f = open('demo.mp3','rb')
info = f.read(44)
import struct
struct.unpack('h','\x01\x02')