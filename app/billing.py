class BillingSystem:
    def calculate_total(self, price: float, quantity: int) -> float:
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative values.")
        return price * quantity