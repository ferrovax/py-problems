# 4.1 Route Between Nodes
def search(graph, start, end):
	# an iterative BFS

	if start == end:
		return True

	q = [start]

	while len(q):
		node = q.pop(0)
		node.visited = True

		for a in node.adjacent:
			if not a.visited:
				if a == end:
					return True
				else:
					q.append(a)

	return False

# bi-directional BFS?
