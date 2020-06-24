def DFS(root):
	stack = [root]

	while len(stack):
		node = stack.pop()
		node.visited = True

		for n in node.adjacent:
			if not n.visited:
				stack.append(n)


# DFS recursive:

# if root == None:
#   return
# root.visited = True
# for node in root.adjacent:
	# if not node.visited:
		# search(node)
