class Player(object):
	def __init__(self,uid,name,status=0,level=1):
		self.uid = uid
		self.name = name
		self.stat = status
		self.level = level

class Player2(object):
	__slots__ = ['uid','name','stat','level']
	def __init__(self,uid,name,status=0,level=1):
		self.uid = uid
		self.name = name
		self.stat = status
		self.level = level

p1 = Player('0001','Jim')
p2 = Player('0001','Jim')
print set(dir(p1))-set(dir(p2))