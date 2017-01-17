from inspect import signature

def typeassert(*ty_args,**ty_kargs):
	def decorator(func):
		sig = signature(func)
		btypes = sig.bind_partial(*ty_args,**kargs).arguments


		def wrappers(*args,**kargs):
			for name,obj in sig.bind(*args,**kargs).arguments.items():
				if name in btypes:
					if not isinstance(obj,btypes[name]):
						raise TypeError(' ')


			return func(*args,**kargs)
		return wrapper
	return decorator

@typeassert(int,str,list)
def f(a,b,c):
	print(a,b,c)

f(1,'abc',[1,2,3])
f(1,2,[1,2,3])