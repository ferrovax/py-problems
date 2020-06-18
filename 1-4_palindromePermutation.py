# 1.4 Palindrome Permutation
def isPermutationOfPalindrome(phrase):
	bitVector = createBitVector(phrase.replace(" ", ""))
	return bitVector == 0 or bitVector & (bitVector - 1) == 0
	# phrase is a permutation of a palindrome if bitvector is zero or has one 1
	# one 1: for instance, 00010000 - 1 = 00001111 => 00010000 & 00001111 = 0

def createBitVector(phrase):
	bitVector = 0
	for c in phrase:
		i = ord(c)
		bitVector = toggle(bitVector, i)
	return bitVector

def toggle(bitVector, index):
	if index < 0:
		return bitVector
	mask = 1 << index
	if bitVector & mask == 0:
		# if no 1s overlap (new character)
		# then add new 1 to the bit vector
		bitVector |= mask
	else:
		# otherwise need to reset position to 0 while keeping other 1s
		# &ing keeps overlapping 1s, use ~mask to reset bit in question and keep the rest
		bitVector &= ~mask
	return bitVector
