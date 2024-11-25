class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Customer: {self.name}, Contact: {self.contact}"
