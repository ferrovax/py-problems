# 2.4 Partition
def partition(node, x):
	# x is an integer value around which to partition the linked list

	head, tail = node, node

	while node:
		next = node.next

		if node.data < x:
			# insert node at head
			node.next = head
			head = node
		else:
			# insert node at tail
			tail.next = node
			tail = node

		node = next

    # don't want a loop
	tail.next = None
    
	return head
