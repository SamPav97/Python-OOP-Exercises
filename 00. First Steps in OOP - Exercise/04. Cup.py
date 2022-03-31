class Cup:
    def __init__(self, size, quantity):
        self.size = int(size)
        self.quantity = int(quantity)

    def fill(self, quantity):
        if self.quantity + int(quantity) > self.size:
            pass
        else:
            self.quantity += int(quantity)

    def status(self):
        return self.size - self.quantity
