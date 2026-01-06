# Constructor Overloading is not allowed in python.
# We use default arguments to inherit overloading characteristics.

class Product:
    def __init__(self, price = 0, discount = 0):
        self.price = price
        self.discount = discount
p1 = Product()
p2 = Product(500)
p3 = Product(500,50)

print(p1.price,p1.discount)
print(p2.price,p2.discount)
print(p3.price,p3.discount)