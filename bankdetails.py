import random

class Account:
    def __init__(self, name, address, mobilenumber, ID, account_number):
        self.name = name
        self.address = address
        self.mobilenumber = mobilenumber
        self.ID = ID
        self.account_number = account_number
        self.balance = 0

class Bank:
    def __init__(self):
        self.accounts = []

    def is_not_empty(self, value):
        return value is not None and value != ""

    def is_available(self, name, address, mobilenumber, ID):
        for account in self.accounts:
            if (account.name == name or
                account.address == address or
                account.mobilenumber == mobilenumber or
                account.ID == ID):
                return False
        return True

    def create_account(self, name, address, mobilenumber, ID):
        if not all([self.is_not_empty(name), self.is_not_empty(address), self.is_not_empty(mobilenumber), self.is_not_empty(ID)]):
            return "Account creation failed: All fields must be provided and not empty."

        if not self.is_available(name, address, mobilenumber, ID):
            return "Account creation failed: Duplicate information detected."

        account_number = self.generate_account_number()
        new_account = Account(name, address, mobilenumber, ID, account_number)
        
        self.accounts.append(new_account)
        return f"Account created successfully with account number: {account_number}"

    def generate_account_number(self):
        return random.randint(10**11, 10**12 - 1)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def make_deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account and amount > 0:
            account.balance += amount
            return f"Deposit successful. New balance: {account.balance}"
        return "Deposit failed. Please check the account number and amount."

    def make_withdrawal(self, account_number, amount):
        account = self.find_account(account_number)
        if account and 0 < amount <= account.balance:
            account.balance -= amount
            return f"Withdrawal successful. New balance: {account.balance}"
        return "Withdrawal failed. Please check the account number and amount."

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            return f"Account balance: {account.balance}"
        return "Account not found."

bank = Bank()

# Creating accounts
print(bank.create_account("Kanishka", "Voltas Colony main road", "986743210", "A12894322"))
kanishka_account_number = bank.accounts[0].account_number
# Making deposits
print(bank.make_deposit(kanishka_account_number, 1000))
# Making withdrawals
print(bank.make_withdrawal(kanishka_account_number, 500))
# Checking balances
print(bank.check_balance(kanishka_account_number))  

