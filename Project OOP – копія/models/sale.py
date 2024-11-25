class Sale:
    def __init__(self, product, quantity, customer):
        self.product = product
        self.quantity = quantity
        self.customer = customer
        self.total_price = product.price * quantity

    def process_sale(self):
        if self.product.quantity >= self.quantity:
            self.product.update_quantity(-self.quantity)
            return f"Sale processed for {self.customer.name}. Total price: {self.total_price} USD"
        else:
            return f"Not enough {self.product.name} in stock for the sale."
