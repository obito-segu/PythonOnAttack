#coding:utf8
#

#python2
f = open('py2.txt','w')
s = u'文本'
f.write(s.encode('utf8'))
f.close()
f = open('py2.txt','r')
t = f.read()
t.decode('utf8')
print t


#python3
f = open('py3.txt','wt',encoding='utf8')
f.write('文本')
f.close()
f = open('py3.txt','rt',encoding='utf8')
s = f.read()
print(s)