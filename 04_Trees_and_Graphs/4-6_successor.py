# 4.6 Successor
# find in-order successor of a given node in a binary search tree
# assume each node has a link to its parent

def inOrderSuccessor(treenode):
	if treenode == None:
		return None

	if treenode.right != None:
		return leftMostChild(treenode.right)
	else:
		x = treenode.parent
		
		while x != None and x.left != treenode:
			treenode = x
			x = x.parent

		return x

def leftMostChild(treenode):
	if treenode == None:
		return None

	while treenode.left != None:
		treenode = treenode.left

	return treenode
