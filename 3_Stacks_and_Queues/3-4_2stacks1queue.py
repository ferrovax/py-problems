# 3.4 Queue via Stacks (make a queue with 2 stacks)
class MyQueue:
	# for the sake of this problem pretend lists can't be popped at index 0
	def __init__(self):
		self.stackNewest = []
		self.stackOldest = []

	def size(self):
		return len(stackNewest) + len(stackOldest)

	def add(self, x):
		self.stackNewest.append(x)

	def peek(self):
		self.shiftStacks()
		return self.stackOldest[len(stackOldest) - 1]

	def remove(self):
		self.shiftStacks()
		return self.stackOldest.pop()

	def shiftStacks(self):
		# only have to shift whenever stackOldest is empty
		if len(stackOldest) == 0:
			while len(stackNewest) > 0:
				stackOldest.append(stackNewest.pop())
