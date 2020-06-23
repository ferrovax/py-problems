# 1.1 Is Unique
def isUnique(string):
	# alternatively could use an array [0]*size_alphabet
	cache = set()
	for c in string:
		if c not in cache:
			cache.add(c)
		else:
			return False
	return True
