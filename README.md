Problems in folders 01 through 17 can be found in [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/).

Problems in 00_Rosalind can be found at [Rosalind](http://rosalind.info/problems/list-view/).

Problems in 00_Foo_Bar: [they](https://foobar.withgoogle.com/) find you.

## Testing Utilities

### Linked Lists
For linked lists something simple like the following will do:
```python
class LinkedListNode(object):
	next = None

	def __init__(self, data):
		self.data = data
```

### Trees and Graphs

#### Trees
A simple way to build trees:
```python
class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data, self.left, self.right = data, left, right

	def __repr__(self):
		return str(self.data)

tree = TreeNode( 20, TreeNode( 10, TreeNode( 5, TreeNode(3), TreeNode(7) ), TreeNode( 15, None, TreeNode(17) ) ), TreeNode( 30 ) )
```

##### Heaps
For heaps I recommend importing `heapq`, which is a min heap. Negative values can be used to achieve what is effectively a max heap.

#### Graphs
As an alternative to an adjacency list I recommend a graph wrapper class for your nodes:
```python
class Graph:
	def __init__(self):
		self.nodes = []

class Node:
	def __init__(self, data):
		self.data = data
		self.visited = False
		self.adjacent = []
```

### Bit Manipulation
Use `bin()` to convert integers into binary strings:
```python
print(bin(42))
>>>'0b101010'
```
