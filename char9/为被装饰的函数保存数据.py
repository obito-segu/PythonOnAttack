from functools import update_wrapper,wraps,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES
def mydecorator(func):
	@wraps(func)
	def wrapper(*args,**kards):
		print 'In wrapper'
		func(*args,**kargs)
	update_wrapper(wrapper,func,('__name__','__doc__'),('__dict__'))
	return wrapper

@mydecorator
def example():
	print 'IN example'


print example.__name__
print example.__doc__
print WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES