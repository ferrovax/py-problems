# 1.9 String Rotation
def isRotation(s1, s2):
	if len(s1) > 0 and len(s1) == len(s2):
		s1s1 = s1 + s1
		return s2 in s1s1
	return False
