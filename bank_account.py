class BankAccount:		# declare a class and give it name User
    def __init__(self):
        self.int_rate = 0.7
        self.balance = 100.00
        # self.name = "BA1"

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.balance -= amount
        if amount > self.balance:
            print ("INVALID TRANSACTION")
        else:
            self.balance-= amount
            print (self.balance)
        return self

    def display_account_info(self):
        print('Balance: ' + '$' + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        else:
            print ("INVALID TRANSACTION")
        return self


jay = BankAccount()
wadeAccount = BankAccount()

jay.make_deposit(200).make_deposit(200).make_deposit(50).make_withdrawal(5).yield_interest().display_account_info()
wadeAccount.make_deposit(40000).make_deposit(200).make_withdrawal(200).make_withdrawal(50).make_withdrawal(5).make_withdrawal(200).yield_interest().display_account_info()



# matthew = User("Matthew Wade", "mat@email.com")
# oliver = User("Oliver Wade", "oli@email.com")