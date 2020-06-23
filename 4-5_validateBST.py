# 4.5 Validate BST

# Solution #1: In-Order Traversal
# this solution does not handle all duplicate cases properly,
# so it is assumed there aren't any
class WrapInt:
	value = None

previous = WrapInt()

def checkBST(tree_node):
	if tree_node == None:
		return True

	# check/recurse left; if left side is not a BST return False
	if not checkBST(tree_node.left):
		return False

	# check current node
	if previous.value != None and previous.value >= tree_node.data:
		return False

	previous.value = tree_node.data

	# check/recurse right; if right side is not a BST return False
	if not checkBST(tree_node.right):
		return False

	return True

# ------------------------------------------------------------------------------

# Solution #2: Min / Max
def check_BST(tree_node):
	return checkMinMax(tree_node, None, None)

def checkMinMax(tree_node, min, max):
	if tree_node == None:
		return True

	if (min != None and tree_node.data <= min) or (max != None and tree_node.data > max):
		return False

	if not checkMinMax(tree_node.left, min, tree_node.data):
		return False

	if not checkMinMax(tree_node.right, tree_node.data, max):
		return False

	return True
