from random import randint,sample

s1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}

print s1
print s2
print s3

#1
res=[]
for k in s1:
	if k in s2 and k in s3:
		res.append(k)
print res

#2
print s1.viewkeys() & s2.viewkeys() & s3.viewkeys()

#n

print reduce(lambda a,b: a & b,map(dict.viewkeys,[s1,s2,s3]))