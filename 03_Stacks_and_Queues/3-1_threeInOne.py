# 3.1 Three in One
class FixedMultiStack:
	numberOfStacks = 3

	def __init__(self, stackSize):
		self.stackCapacity = stackSize
		self.values = [None] * (stackSize * self.numberOfStacks)
		self.sizes = [0] * self.numberOfStacks

	def push(self, stackNum, value):
		if self.isFull(stackNum):
			raise Exception('That stack is full')

		self.sizes[stackNum] += 1
		self.values[self.indexOfTop(stackNum)] = value

	def pop(self, stackNum):
		if self.isEmpty(stackNum):
			raise Exception('That stack is empty')

		topIndex = self.indexOfTop(stackNum)
		value = self.values[topIndex]

		self.values[topIndex] = None
		self.sizes[stackNum] -= 1

		return value

	def peek(self, stackNum):
		if self.isEmpty(stackNum):
			raise Exception('That stack is empty')

		return self.values[self.indexOfTop(stackNum)]

	def isEmpty(self, stackNum):
		return self.sizes[stackNum] == 0

	def isFull(self, stackNum):
		return self.sizes[stackNum] == self.stackCapacity

	def indexOfTop(self, stackNum):
		# returns index of the top of the given stack

		offset = stackNum * self.stackCapacity
		size = self.sizes[stackNum]

		return offset + size - 1
