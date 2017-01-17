class IntTuple(tuple):
	def __new__(cls,iterable):
		g = (x for x in iterable if isinstance(x,int) and x>0)
		return super(IntTuple,cls).__new__(cls,g)
	# def __init__(self,iterable):
	# 	super(IntTuple,self).__init__(iterable)


t = IntTuple([1,-1,'ab',6,[1,2],3])
print t