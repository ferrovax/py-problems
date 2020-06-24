# 2.3 Delete Middle Node (a node somewhere in the middle)
def deleteMidNode(n):
	if n == None or n.next == None:
		return False

	n.data = n.next.data
	n.next = n.next.next
