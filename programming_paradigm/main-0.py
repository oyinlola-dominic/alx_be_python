import sys
from bank_account import BankAccount

def _fmt_amt(a):
    """Return string formatted amount: integer if whole, otherwise trimmed decimals."""
    try:
        f = float(a)
    except (ValueError, TypeError):
        return str(a)
    if f.is_integer():
        return str(int(f))
    s = f"{f:.2f}".rstrip('0').rstrip('.')
    return s

if __name__ == "__main__":
    # initial balance as per the example in the task description
    account = BankAccount(100)

    # Minimal argument checking consistent with example behavior
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = params[0] if params else None

    if command == "deposit" and amount is not None:
        try:
            amt = float(amount)
        except (ValueError, TypeError):
            sys.exit(1)
        account.deposit(amt)
        print(f"Deposited: ${_fmt_amt(amt)}")
    elif command == "withdraw" and amount is not None:
        try:
            amt = float(amount)
        except (ValueError, TypeError):
            sys.exit(1)
        if account.withdraw(amt):
            print(f"Withdrew: ${_fmt_amt(amt)}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
