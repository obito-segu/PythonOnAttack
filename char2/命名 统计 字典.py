'''
naming for tuple
'''
#1
NAME,AGE,SEX,EMAIL = xrange(4)
student = ('snow',16,'m','momo@gmail.com')
print student[NAME],student[AGE],student[SEX],student[EMAIL]

#2
from collections import namedtuple
Student = namedtuple('Student',['name','age','sex','email'])
s = Student('snow',16,'m','momo@gmail.com')
print s.name,s.age,s.sex,s.email
print isinstance(s,tuple)

'''
counting element
'''
from random import randint
data = [randint(0,20) for _ in xrange(30)]
print data
#1.1
c = dict.fromkeys(data,0)
for x in data:
	c[x]+=1
print c
#1.2
from collections import Counter
c2 = Counter(data)
print c2,c2.most_common(3)

#2
import re
txt = open('yoyo.txt').read()

print re.split('\w+',txt)
c3 = Counter(re.split('\w+',txt))
print c3,c3.most_common(10)


'''
sorting in dict
'''
from random import randint
d = {x:randint(60,100) for x in 'abcxyz'}
print sorted(d)
#1
print zip(d.values(),d.keys())

#2
print sorted(d.items(), key=lambda x:x[1])