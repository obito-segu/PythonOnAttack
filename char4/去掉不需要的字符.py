s = '\tabc\t123\txyz\ropq\r'
import re
print re.sub('[\t\r]','',s)


str.translate
s = 'abc123023xyz'
import string
print s.translate(string.maketrans('abcxyz','xyzmnl'))
