s = 'abc'
print s.ljust(20,'-')
print s.center(20)
print s.rjust(20,'*')

print format(s,'<20')
print format(s,'^20')
print format(s,'>20')