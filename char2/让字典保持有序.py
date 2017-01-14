

from collections import OrderedDict
d = OrderedDict()
d['jim'] = (1,35)
d['tom'] = (2,37)
d['sam'] = (3,40)
for k in d:
	print k

####################################################
from time import time
from random import randint
from collections import OrderedDict

d=OrderedDict()
players = list('abcdefgh')
start = time()

for i in xrange(8):
	raw_input()
	p = players.pop(randint(0,7-i))
	end = time()
	print i+1,p,end-start
	d[p] = (i+1,p,end-start)

print '.'*20
for k in d:
	print k,d[k]