class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price
    
order1 = Order("Laptop", 1200)
order2 = Order("Phone", 800)

print(order1 > order2)  # Output: True, because 1200 > 800