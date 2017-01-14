'''
list
'''
from random import randint

list = [randint(-10,10) for _ in xrange(10)]
print list

#1
print filter(lambda x: x>0,list)
# timeit filter(lambda x: x>0,list)

#2
print [x for x in list if x>0]
# timeit [x for x in list if x>0]


'''
dict
'''
dict = {x: randint(60,100) for x in xrange(1,21)}
print dict

print {k:v for k,v in dict.iteritems() if v > 90}



'''
collection
'''
s = set(list)
print s
print {x for x in s if x%3 == 0}
