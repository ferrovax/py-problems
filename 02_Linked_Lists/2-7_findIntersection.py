# 2.7 Intersection
def findIntersection(list1, list2):
	if list1 == None or list2 == None:
		return None

	# get tails and sizes
	result1 = getTailAndSize(list1)
	result2 = getTailAndSize(list2)

	# if different tails then there is no intersection
	if result1.tail != result2.tail:
		return None

	# set pointers to start of each linked list
	shorter = list1 if result1.size < result2.size else list2
	longer = list2 if result1.size < result2.size else list1

	# advance pointer of longer list
	longer = getKthNode(longer, abs(result1.size - result2.size))

	# move both pointers until collision
	while shorter != longer:
		shorter = shorter.next
		longer = longer.next
        
	# return either of them
	return shorter

class Result:
	def __init__(self, tail, size):
		self.tail = tail
		self.size = size

def getTailAndSize(list):
	if list == None:
		return None

	size, current = 1, list

	while current.next != None:
		size += 1
		current = current.next

	return Result(current, size)

def getKthNode(head, k):
	current = head

	while k > 0 and current != None:
		current = current.next
		k -= 1

	return current
