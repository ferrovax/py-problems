# 4.3 List of Depths
# Given a binary tree, create linked lists for each tree level

### One solution: ###

# recursive approach (a modification of pre-order traversal using DFS)

def DFS_createLevelLinkedList(root):
	lists = []
	createLevelLinkedList(root, lists, 0)
	return lists

def createLevelLinkedList(root, lists, level):
	if root == None:
		return

	if len(lists) == level:
		# the binary tree level we are at is not in our list of linked lists
        # add a new Linked List to lists
		lists.append(LinkedListWrapper())

	# pre-order traversal
    # add a new linked list node with current TreeNode's data to appropriate linked list
	lists[level].add( LinkedListNode(root.data) )

    # recurse left
	createLevelLinkedList(root.left, lists, level + 1)

    # recurse right
	createLevelLinkedList(root.right, lists, level + 1)

# ------------------------------------------------------------------------------

### Alternatively: ###

# iterative approach (modified BFS)

def BFS_createLevelLinkedList(root):
	result = []

    # add root to queue
	q = [root]

    # make first level's linked list
	ll = LinkedListWrapper()
	ll.add(LinkedListNode(root.data))

	while len(q) > 0:
        # the queue contains a tree level
        # add latest linked list to result
		result.append(ll)

        # start a fresh linked list
		ll = LinkedListWrapper()

        # a temp for updating the queue
		temp = []

		for parent in q:
			if parent.left != None:
				ll.add(LinkedListNode(parent.left.data))
				temp.append(parent.left)

			if parent.right != None:
				ll.add(LinkedListNode(parent.right.data))
				temp.append(parent.right)

        # update queue (to contain the child nodes)
		q = temp

	return result

# ------------------------------------------------------------------------------

class LinkedListWrapper:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, node):
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def size(self):
		if self.head == None:
			return 0

		size, h = 1, self.head

		while h.next != None:
			size += 1
			h = h.next

		return size
