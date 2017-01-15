s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'

print s

#1
def mySplit(s,ds):
	res = [s]

	for d in ds:
		t = []
		map(lambda x:t.extend(x.split(d)),res)
		res = t
	return [x for x in res if x]

print mySplit(s,',;|\t')

#2
import re
print re.split(r'[,;\t|]+',s)