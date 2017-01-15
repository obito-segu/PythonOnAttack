from random import randint
cn = [randint(60,100) for _ in xrange(40)]
math = [randint(60,100) for _ in xrange(40)]
eg = [randint(60,100) for _ in xrange(40)]

total = []
for c,m,e in zip(cn,math,eg):
	total.append(c + m + e)

print total


from itertools import chain
a = [randint(60,100) for _ in xrange(40)]
b = [randint(60,100) for _ in xrange(30)]
c = [randint(60,100) for _ in xrange(50)]
d = [randint(60,100) for _ in xrange(20)]

count = 0
for s in chain(a,b,c,d):
	if s > 90:
		count+=1

print count