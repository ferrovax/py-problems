# 3.2 Stack Min
class StackWithMin:
	def __init__(self):
		self.stack = []
		self.mins = []
		self.size = 0

	def push(self, x):
		self.stack.append(x)

		if self.size == 0 or x < self.mins[self.size - 1]:
			self.mins.append(x)
		else:
			self.mins.append(self.mins[self.size - 1])

		self.size += 1

	def pop(self):
		if self.size > 0:
			self.size -= 1
			self.mins.pop()
            
			return self.stack.pop()
		else:
			raise Exception('Empty stack')

	def min(self):
		return self.mins[self.size - 1]
