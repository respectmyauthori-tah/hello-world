class Polynomial(object):
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial(*{!r}'.format(self.coeffs)

	def __add__(self, other):
		return Polynomial(*(x + y for x, y in zip (self.coeffs, other.coeffs)))	

p1 = Polynomial(1, 2, 3) #x
p2 = Polynomial(3, 4, 3)		