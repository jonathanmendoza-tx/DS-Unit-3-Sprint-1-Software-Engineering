import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
	"""
	Making sure Acme products are the tops!
	"""
	def test_default_product_price(self):
		"""
		Test default product price being 10.
		"""
		prod = Product('Test Product')
		self.assertEqual(prod.price, 10)

	def test_default_product_weight(self):
		"""
		Test default product weight being 20.
		"""
		prod = Product('Test Product')
		self.assertEqual(prod.weight, 20)

	def test_stealability_explode(self):
		"""
		Test stealability and explode function with other than default
		values
		"""
		prod = Product('Test Product')

		prod.weight = 100
		prod.price = 1000

		self.assertEqual(Product.stealability(prod), 'Very stealable!')
		self.assertEqual(Product.explode(prod),'...BABOOM!!')



class AcmeReportTests(unittest.TestCase):

	def test_default_num_products(self):
		"""
		Test that products really does receive a list of default length 30
		"""
		products = generate_products()

		self.assertEqual(len(products), 30)

	def test_legal_names(self):
		"""
		checks that the generated names for a default batch of products
		are all valid possible names to generate (adjective, space, noun,
		from the lists of possible words)
		"""
		products = generate_products()

		check_for_adj = []
		check_for_noun = []

		for i in range(len(products)): 
			"""
			Split and collect the first and second words of each product in
			a list. Check if the first names match to adjectives and the second
			to nouns
			"""
			name = str(products[i]).split()

			check_for_adj += [name[0]]
			check_for_nouns += [name[1]]

		for j in range(len(set(check_for_adj))):
			self.assertIn(list(set(check_for_adj))[j], ADJECTIVES)

		for k in range(len(set(check_for_noun))):
			self.assertIn(list(set(check_for_nouns))[k], NOUNS)


if __name__ == '__main__':
	unittest.main()
