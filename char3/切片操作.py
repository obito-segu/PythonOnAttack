#iter(l)
#l.__iter__
#
#reversed(l)
#l.__reversed__
#
class FloatRange:
	def __init__(self,start,end,step=0.1):
		self.start = start
		self.end = end
		self.step = step

	def __iter__(self):
		t = self.start
		while t <= self.end:
			yield t
			t += self.step

	def __reversed__(self):
		t = self.end
		while t >= self.start:
			yield t
			t-=self.step

for x in FloatRange(1.,4.,.5):
	print x

for x in reversed(FloatRange(1.,4.,.5)):
	print x