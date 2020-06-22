# 4.2 Minimal Tree
# make a minimal height BST from a SORTED array of integers

def createMinimalBST(ints):
	return createMinBST(ints, 0, len(ints) - 1)

def createMinBST(ints, start, end):
	if end < start:
		return None

	mid = (start + end) // 2
	node = TreeNode(ints[mid])

	node.left = createMinBST(ints, start, mid - 1)
	node.right = createMinBST(ints, mid + 1, end)
    
	return node
