class CashRegister:
    def __init__(self, discount=0):
        self._total = 0
        self.discount = discount
        self._items = []

    def add_item(self, title, price, quantity=1):
        self._items.append((title, price, quantity))
        self._total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self._total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${self._total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self._items:
            # Modified logic starts here
            # If there's only one item, subtract its total cost from the total
            if len(self._items) == 1:
                title, price, quantity = self._items[0]
                self._total -= price * quantity
            # If there are multiple items, subtract the cost of the last item
            else:
                title, price, quantity = self._items[-1]  # Get the last item
                self._total -= price * quantity  # Subtract its cost from the total
                # Optionally, clear the register if you want to remove all traces of the transaction
                # self._items.clear()  # Uncomment this line if you decide to clear the register
            # Modified logic ends here

    def reset_register_totals(self):
        self._total = 0
        self._items.clear()

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def items(self):
        # Return a list of item names repeated according to the quantity
        return [title for title, _, quantity in self._items for _ in range(quantity)]

    @items.setter
    def items(self, value):
        self._items = value
