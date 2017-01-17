from functools import total_ordering
@total_ordering
from math import pi
class Circle(object):
	def __init__(self, radius):
		self.radius = radius
	def getRadius(self):
		return self.radius
	def setRadius(self,value):
		if not isinstance(value,(int,long,float)):
			raise ValueError('wrong type')
		self.radius = float(value)
	def getArea(self):
		return self.radius ** 2 * pi
	R = property(getRadius,setRadius)
c = Circle(3.2)
c.setRadius(3.2)
c.R = 5.9
print c.getRadius(),c.getArea()
print c.R


###########################################33
class Rectangle(object):
	def __init__(self,w,h):
		self.w = w
		self.h = h
	def area(self):
		return self.w * self.h
	def __lt__(self,obj):
		print 'in__lt__'
		return self.area() < obj.area()

	def __le__(self,obj):
		print 'in__le__'
		return self.area() <= obj.area()

r1 = Rectangle(5,3)
r2 = Rectangle(4,4)
print r1 < r2
