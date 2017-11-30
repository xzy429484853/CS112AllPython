#define function
def each_kind(a,b,c):
	# A is positive
	if a > 0:
		if b == 0:
			if c < 0:
				return True
			else:
				return False
		elif c == 0:
			if b < 0:
				return True
			else:
				return False
		else:
			return False
				
	# B is positive			
	elif b > 0:
		if a == 0:
			if c < 0:
				return True
			else:
				return False
		elif c == 0:
			if a < 0:
				return True
			else:
				return False
		else:
			return False
				
	# C is positive
	elif c > 0:
		if a == 0:
			if b < 0:
				return True
			else:
				return False
		elif b == 0:
			if a < 0:
				return True
			else:
				return False
		else:
			return False
	else:
		return False
		
#run function
#each_kind(a,b,c)
