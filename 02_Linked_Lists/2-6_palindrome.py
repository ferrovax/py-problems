# 2.6 Palindrome
def isPalindrome(head):
	fast, slow, stack = head, head, []

	while fast and fast.next:
		# push elements from first half of the linked list onto the stack
		stack.append(slow.data)

		slow = slow.next
		fast = fast.next.next

	if fast:
		# there's an odd number of nodes, skip the middle one
		slow = slow.next

	while slow:
		if stack.pop() != slow.data:
			return False

		slow = slow.next

	return True
