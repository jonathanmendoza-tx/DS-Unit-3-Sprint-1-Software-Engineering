from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 
				'Portable', 'Improved']

NOUNS = ['Anvil', 'Catapult', 'Disguise', 
				'Mousetrap', '???']


def generate_products(num_products=30):
	"""
	Generates a list with a passed number of products (default = 30)
	"""
	products = []

	for _ in range(num_products):
		adj_rand = ADJECTIVES[randint(0, len(ADJECTIVES)-1)]
		noun_rand = NOUNS[randint(0, len(NOUNS)-1)]

		name = adj_rand+" "+noun_rand
		weight = randint(5, 100)
		price = randint(5, 100)
		flammability = uniform(0,2.5)

		products.append(Product(name = name, weight = weight, price = price, flammability = flammability))
			
	return products


def inventory_report(products):
	""" Prints an inventory report using random values for prices,
	weights and flammability.  
	"""
	print('ACME CORPORATION OFFICIAL INVENTORY REPORT\n')

	print(f'Unique product names: {len(set(products))}')

	prices = []
	weights = []
	flammabilities = []

	for i in range(len(products)):
		prices += [products[i].price]
		weights += [products[i].weight]
		flammabilities += [products[i].flammability]

	avg_price = sum(prices)/len(prices)
	avg_weight = sum(weights)/len(weights)
	avg_flamm = sum(flammabilities)/len(flammabilities)

	print(f'Average price: {avg_price}')
	print(f'Average weight: {avg_weight}')
	print(f'Average flammability: {avg_flamm}')


if __name__ == '__main__':
	inventory_report(generate_products())
