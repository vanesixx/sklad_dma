class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            print(f"({self.account_holder}) Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposit accepted. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount < 0:
            print(f"({self.account_holder})Withdraw amount must be positive")
            return

        if amount > self.__balance:
            print("Insufficient funds.")
            return

        self.__balance -= amount
        print(f"Withdraw accepted. New balance: {self.__balance}")

    def transfer(self, other_account, amount):
        if amount < 0:
            print(f"({self.account_holder})Transfer amount be positive.")
            return
        if amount > self.__balance:
            print("Insufficient funds for transfer.")
            return
        self.__balance -= amount
        other_account.__balance += amount
        print(f"({self.account_holder} > {other_account.account_holder})Transfer accepted. New balance: {self.__balance}")


bank_accounts = [BankAccount("Jan", 1000)]

class ATM:
    def __init__(self, accounts):
        self.accounts = accounts

    def print_accounts(self):
        i = 0
        for bank_account in self.accounts:
            print(f"{i} - {bank_account.account_holder}")
            i += 1
        menu()

    def add_account(self):
        name = input("Název účtu: ")
        self.accounts.append(BankAccount(name))
        menu()

    def transfer(self):
        print("Dostupné účty:")
        self.print_accounts()

        index_from = int(input("Účet ze kterého: "))
        index_to = int(input("Účet do kterého: "))
        amount = float(input("Částka: "))

        self.accounts[index_from].transfer(self.accounts[index_to], amount)
        menu()

    def deposit(self):
        print("Dostupné účty:")
        self.print_accounts()

        index_to = int(input("Účet do ktereho:"))
        amount = float(input("Částka: "))

        self.accounts[index_to].deposit(amount)
        menu()

    def withdraw(self):
        print("Dostupné účty:")
        self.print_accounts()

        index_from = int(input("Účet ze kterého : "))
        amount = float(input("Částka: "))

        self.accounts[index_from].withdraw(amount)
        menu()


atm = ATM(bank_accounts)

def menu():
    print("Vítejte v bance!")
    print("1 - seznam účtů")
    print("2 - přidat účet")
    print("3 - převod financí")
    print("4 - výběr financí")
    print("5 - vklad financí")

    choice = int(input("Zvolte akci:"))
    if choice == 1:
        atm.print_accounts()
    elif choice == 2:
        atm.add_account()
    elif choice == 3:
        atm.transfer()
    elif choice == 4:
        atm.withdraw()
    elif choice == 5:
        atm.deposit()
    else:
        print("Chybná akce, výběr znovu")

menu()
