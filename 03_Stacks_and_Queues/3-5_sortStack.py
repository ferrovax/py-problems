# 3.5 Sort Stack
# can use one additional stack but no other data structures

def sortStack(stack):
	# O(n^2) time and O(n) space

	bufferStack = []

	while len(stack) > 0:
		temp = stack.pop()

		while len(bufferStack) > 0 and bufferStack[len(bufferStack) - 1] > temp:
			stack.append(bufferStack.pop())

		bufferStack.append(temp)

	# coppy elements from buffer back to stack
	while len(bufferStack) > 0:
		stack.append(bufferStack.pop())
