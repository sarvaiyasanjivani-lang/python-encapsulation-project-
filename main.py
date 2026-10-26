
from bank_account import BankAccount


def main():
    account = BankAccount("Sanjivani", 7000)

    account.deposit(700)
    account.withdraw(800)

    print("Account holder:", account.owner)
    print("Current balance:", account.get_balance())


if __name__ == "__main__":
    main()
