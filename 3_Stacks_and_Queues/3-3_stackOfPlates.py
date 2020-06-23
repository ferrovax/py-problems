# 3.3 Stack of Plates
class SetOfStacks:

	def __init__(self, capacity):
		self.stacks = [[]]
		self.size = 1
		self.capacity = capacity

	def push(self, x):
		stackNum = self.size - 1

		if len(self.stacks[stackNum]) == self.capacity:
			self.stacks.append([x])
			self.size += 1
		else:
			self.stacks[stackNum].append(x)

	def pop(self):
		stackNum = self.size - 1
		result = self.stacks[stackNum].pop()

		if len(self.stacks[stackNum]) == 0:
			self.stacks.pop()
			self.size -= 1

		return result

	def popAt(self, index):
		return self.stacks[index].pop()
