# def fibnacci(n,cache=None):
# 	if cache is None:
# 		cache = {}
# 	if n in cache:
# 		return cache[n]

# 	if n <= 1:
# 		return 1
# 	cache[n] = fibnacci(n - 1,cache) + fibnacci(n - 2,cache)
# 	return cache[n]
def memo(func):
	cache = {}
	def wrap(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]

	return wrap




@memo
def fibnacci(n):
	

	if n <= 1:
		return 1
	return fibnacci(n - 1) + fibnacci(n - 2)
	


################################

@memo
def climb(n,steps):
	count = 0
	if n == 0:
		count = 1
	elif n > 0:
		for step in steps:
			count += climb(n - step,steps)
	return count

print fibnacci(50)
print climb(10,(1,2,3))