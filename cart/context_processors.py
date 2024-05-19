from .cart import Cart


# sakht context processor ta dar tamam safahat betune kar kone
def cart(request):
	# data i ke dar Cart vojud dare ro barmigardune
	return {'cart': Cart(request)}



