import sys
from bank_account import BankAccount

if __name__ == "__main__":
    account = BankAccount(0)

    if len(sys.argv) < 2:
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
