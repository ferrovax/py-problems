def BFS(root):
	q = [root]
    
	while len(q):
		node = q.pop(0)
		node.visited = True

		for n in node.adjacent:
			if not n.visited:
				q.append(n)
