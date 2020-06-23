# 3.6 Animal Shelter
class AnimalShelter:
	def __init__(self):
		self.dogs = []
		self.cats = []
		self.priority = 0

	def enqueue(self, animal):
		if isinstance(animal, Dog):
			animal.priority = self.priority
			self.priority += 1
			self.dogs.append(animal)
		elif isinstance(animal, Cat):
			animal.priority = self.priority
			self.priority += 1
			self.cats.append(animal)
		else:
			raise Exception('We only take Dogs or Cats')

	def dequeueAny(self):
		dog, cat = self.dogs[0], self.cats[0]

		if dog.priority < cat.priority:
			return self.dequeueDog()
		else:
			return self.dequeueCat()

	def dequeueDog(self):
		return self.dogs.pop(0)

	def dequeueCat(self):
		return self.cats.pop(0)

class Animal:
	def __init__(self, name):
		self.name = name
		self.priority = None

class Dog(Animal):
	def __repr__(self):
		return '%s -- Dog' % self.name

class Cat(Animal):
	def __repr__(self):
		return '%s -- Cat' % self.name
