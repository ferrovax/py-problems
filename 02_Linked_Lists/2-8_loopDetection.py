# 2.8 Loop Detection
def findLoopBeginning(head):
	slow, fast = head, head

	# find where the pointers meet
    # this will be LOOP_SIZE - k steps into the loop (where k is the size of the non-looped region)
	while fast != None and fast.next != None:
		slow = slow.next
		fast = fast.next.next

        # break upon collision
		if slow == fast:
			break

	# if there isn't a loop return None
	if fast == None or fast.next == None:
		return None

	# move slow back to the head, keep fast at collision point
    slow = head

    # both slow and fast are k from the start of loop, so step each forward to find it
	while slow != fast:
		slow = slow.next
		fast = fast.next

	# return either pointer
	return fast
