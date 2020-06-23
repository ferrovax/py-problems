# 2.5 Sum Lists

# EXAMPLE
# 617 + 295 = 912
# Input: ( 7 -> 1 -> 6 ) + ( 5 -> 9 -> 2 )
# Output: ( 2 -> 1 -> 9 )
# (linked lists begin with ones place)

def sumLists(l1, l2, carry):
	if l1 == None and l2 == None and carry == 0:
		# recursive base case; None is the tail's next so we return it here
		return None

	result = LinkedListNode(0)
	value = carry

	if l1 != None:
		value += l1.data

	if l2 != None:
		value += l2.data

	result.data = value % 10

	if l1 != None or l2 != None:
		more = sumLists(None if l1 == None else l1.next, None if l2 == None else l2.next, 1 if value >= 10 else 0)
		result.next = more

	return result



# Follow Up:

# EXAMPLE
# 617 + 295 = 912
# Input: ( 6 -> 1 -> 7 ) + ( 2 -> 9 -> 5 )
# Ouptut: ( 9 -> 1 -> 2 )
# (linked list orders reversed to read left to right)

def sumLists(l1, l2):
	len1, len2 = length(l1), length(l2)

	# Pad the shorter list with zeroes
	if len1 < len2:
		l1 = padList(l1, len2 - len1)
	else:
		l2 = padList(l2, len1 - len2)

	sum = sumListsHelper(l1, l2)

	if not sum.carry:
		return sum.sum
	else:
		return insertBefore(sum.sum, sum.carry)


def sumListsHelper(l1, l2):
	if l1 == None and l2 == None:
		sum = PartialSum()
		return sum

	# add recursively
	sum = sumListsHelper(l1.next, l2.next)

	# add carry to current data
	val = sum.carry + l1.data + l2.data

	# insert sum of current digits
	full_result = insertBefore(sum.sum, val % 10)

	# update sum so far and pass carry value along as well
	sum.sum = full_result
	sum.carry = val // 10

	return sum

class PartialSum:
	sum = None # will be a LinkedListNode
	carry = 0

def padList(l, padding):
	head = l

	for i in range(padding):
		head = insertBefore(head, 0)

	return head

def insertBefore(l, data):
	node = LinkedListNode(data)

	if l:
		node.next = l

	return node

def length(l):
	count = 0

	while l:
		count += 1
		l = l.next

	return count
