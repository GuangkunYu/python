from CreditCard import CreditCard


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    
    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new credit card instance
        
        The initial balance is zero

        customer: the name of the customer(e.g: 'John Bowman')
        bank: the name of the bank(e.g: 'California Savings')
        acnt: the acount identifier(e.g: '5391 0375 9387 5309') 
        limit: credit limit(measured in dollars)
        apr: annual percentage rate(e.g: 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to card, assuming sufficient credit limit.

        Return True if charge was processed; 
        Return False and assess $5 fee if charge denied.
        """
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor


if __name__ == "__main__":
    pc = PredatoryCreditCard('John Doe', '1st Bank', '5391 0274 9831 3291', 2500, 0.0825)
    print(pc)
