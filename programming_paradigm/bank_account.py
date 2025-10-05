class BankAccount:
    def __init__(self, balance=0):
        # store as float internally for correct arithmetic
        self.balance = float(balance)

    def deposit(self, amount):
        """Add amount to balance. No return value expected."""
        try:
            amt = float(amount)
        except (ValueError, TypeError):
            return
        if amt < 0:
            return
        self.balance += amt

    def withdraw(self, amount):
        """
        Attempt to withdraw amount.
        Returns True if successful, False otherwise (insufficient funds or invalid input).
        """
        try:
            amt = float(amount)
        except (ValueError, TypeError):
            return False
        if amt <= self.balance:
            self.balance -= amt
            return True
        return False

    def display_balance(self):
        """
        Print the balance in the expected format:
        Current Balance: $<amount>
        Use an integer display when the amount is whole, otherwise show up to 2 decimal places trimmed.
        """
        if self.balance.is_integer():
            print(f"Current Balance: ${int(self.balance)}")
        else:
            # format with up to 2 decimal places and strip trailing zeros
            s = f"{self.balance:.2f}".rstrip('0').rstrip('.')
            print(f"Current Balance: ${s}")
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")
