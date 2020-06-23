# 4.4 Check Balanced (is given binary tree balanced?)
def isBalanced(root):
	# error code (-9) chosen arbitrarily
	return checkHeight(root) != -9
    
def checkHeight(root):
	if root == None:
		return -1

	leftHeight = checkHeight(root.left)

	if leftHeight == -9:
        # pass error up
		return -9

	rightHeight = checkHeight(root.right)

	if rightHeight == -9:
        # pass error up
		return -9

	heightDiff = abs(leftHeight - rightHeight)

	if heightDiff > 1:
        # found error, pass it back
		return -9
	else:
		return max(leftHeight, rightHeight) + 1
