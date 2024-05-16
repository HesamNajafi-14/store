from photostore.models import Product



class Cart():
	def __init__(self, request):
		self.session = request.session

		# aghar sessiony vogud dash migirimesh
		cart = self.session.get('session_key')

		# aghr karbar jadid bud yeki barash misazim
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}

		# motmaen shavim cart dar tamam safahat site dar dastres ast
		self.cart = cart

	def add(self, product, quantity):
		product_id = str(product.id)
		product_qty = str(quantity)


		if product_id in self.cart:
			pass
		else:
			# self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)
		self.session.modified = True

	def __len__(self):
		return len(self.cart)

	def get_prods(self):
		# gereftan id ha az cart
		product_ids = self.cart.keys()

		# az id baraye peyda kardane mahsulat dar database estefade mikonim
		products = Product.objects.filter(id__in=product_ids)

		return products

	def get_quants(self):
		quantities = self.cart
		return quantities

	def update(self, product, quantity):
		product_id = str(product)
		product_qty = int(quantity)

		ourcart = self.cart

		ourcart[product_id] = product_qty

		self.session.modified = True

		thing = self.cart
		return thing




