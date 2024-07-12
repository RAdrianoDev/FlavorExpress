class Account:
    bank = []

    def __init__(self, holder_name, balance):
        self._holder_name = holder_name
        self._balance = balance
        self._active = False
        Account.bank.append(self)
    
    def __str__(self):
        return f'{self._holder_name} - {self._balance}'
    
    def activate_account(self):
        self._active = True

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):
        return self._balance
    
    @classmethod
    def list_accounts(cls):
        print(f'{"*** Holder Name ***".ljust(25)} | {"*** Balance ***"} | *** Active ***')
        for account in cls.bank:
            print(f'{account._holder_name.ljust(25)} | {account._balance} | {account.active}')
    
    @property
    def active(self):
        return '☒' if self._active else '☐'
    
    def activate(self):
        self._active = not self._active

account_1 = Account('Mew Suppasit', 1000)
account_1.activate_account()

account_2 = Account('Alice', 2000)

account_3 = Account('Singto Prachaya', 3000)
account_3.activate_account()

account_4 = Account('Bright', 4000)

account_5 = Account('Mallory', 5000)

account_6 = Account('Ronaldo Adriano', 6000)
account_6.activate_account()
account_6.deposit(10000)

Account.list_accounts()
