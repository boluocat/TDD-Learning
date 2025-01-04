
class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class LineItem:
    
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        
    def total(self):
        return self.product.price * self.quantity
    
class Cart:
    
    def __init__(self):
        self.line_items: [LineItem] = []
        
    def add_product(self, product: Product, quantity: int):
        self.line_items.append(LineItem(product, quantity))
        
    def get_total(self) -> int:
        total = 0
        for line in self.line_items:
            total += line.product.price * line.quantity
            
        return total
    
    def remove(self, line_item_number: int):
        self.line_items.remove(self.line_items[line_item_number - 1])
        
    def update_quantity(self, line_item_number: int, updated_quantity: int):
        self.line_items[line_item_number - 1].quantity = updated_quantity
    
    def __str__(self):
        output = []
        for line in self.line_items:
            output.append(f"{line.quantity} {line.product_name} {line.product.price} = {line.get_extended_price()}")
        output.append(f"total: {self.get_total()}")
        return "\n".join(output)
    
    
def test_cart():
    cart = Cart()
    product1 = Product("apple", 1)
    product2 = Product("banana", 2)
    cart.add_product(product1, 5)
    cart.add_product(product2, 10)
    assert cart.get_total() == 25
    cart.update_quantity(1, 10)
    assert cart.get_total() == 30
    cart.remove(1)
    assert cart.get_total() == 20
    print("All tests pass")

test_cart()