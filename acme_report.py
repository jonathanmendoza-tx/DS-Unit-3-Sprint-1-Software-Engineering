from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    for _ in range(num_products):
    	adj_rand = ADJECTIVES[randint(0,len(ADJECTIVES)-1)]
    	noun_rand = NOUNS[randint(0,len(NOUNS)-1)]
    	products += adj_rand+" "+noun_rand
    return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())