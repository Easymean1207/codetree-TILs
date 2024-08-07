class Product:
    def __init__(self, name="", code=0):
        self.name = name
        self.code = code


product1 = Product("codetree", 50)
print(f"product {product1.code} is {product1.name}")

given_name, given_code = tuple(input().split())
given_code = int(given_code)
product2 = Product(given_name, given_code)
print(f"product {product2.code} is {product2.name}")