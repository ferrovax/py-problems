# 2.2 Return Kth to Last
def kthToLast(head, k):
	# recursive and iterative approaches both O(n) time,
	# but iterative approach constant O(1) space beats recursive O(n) space

	p1, p2 = head, head

    # move p1 k ahead of p2
	for i in range(k):
		if p1 == None:
            # out of bounds
			return None

		p1 = p1.next

	while p1:
		p1 = p1.next
		p2 = p2.next

	return p2
