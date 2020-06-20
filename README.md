The vast majority of these problems can be found in [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/), which is a book written in Java and English.

My solutions are in Python and English, which, I think, is more clear.

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

```python
```
