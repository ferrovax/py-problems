# 2.1 Remove Dups
def deleteDups(node):
	buff = set()
	prev = None
	while node:
		if node.data in buff:
            # set previous node's next forward one, skipping this duplicate we found
			prev.next = node.next
		else:
            # new data, update buffer and previous
			buff.add(node.data)
			prev = node

		node = node.next

# Follow-Up: without buffer?
def deleteDupsNoBuffer(head):
	# O(n^2) instead of O(n)
	current = head

	while current:
		runner = current

		while runner.next:
            # check rest of linked list
			if runner.next.data == current.data:
				runner.next = runner.next.next
			else:
				runner = runner.next

		current = current.next
