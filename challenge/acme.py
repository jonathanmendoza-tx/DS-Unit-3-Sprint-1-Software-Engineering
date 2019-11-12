class Product:

	from random import randint

	id = random.randint(1000000,9999999)

	def __init__(self, name, price = 10, weight = 20, flammability = 0.5, identifier = id):
		self.name = name
		self.price = price
		self.weight = weight
		self.flammability = flammability
		self.identifier = identifier

	def __repr__(self):
		return f'{self.name}'

	def stealability(self):
		steal = self.price/self.weight

		if steal < 0.5:
			return f'Not so stealable...'

		if (steal >= 0.5) & (steal < 1):
			return f'Kinda stealable.'
		else:
			return f'Very stealable!'

	def explode(self):
		boom = self.flammability*self.weight

		if boom < 10:
			return f'...fizzle.'

		if (boom >= 10) & (boom < 50):
			return f'...boom!'
		else:
			return f'...BABOOM!!'


class BoxingGlove(Product):

	def __init__(self, name, weight = 10):
		super().__init__(name)
		self.weight = weight

	def explode(self):
		return f"...it's a glove."

	def punch(self):
		if self.weight < 5:
			return f'That tickles.'
	
		if (self.weight >= 5) & (self.weight < 15):
			return f'Hey that hurt!'
		else:
			return f'OUCH!'
