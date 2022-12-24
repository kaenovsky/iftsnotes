# polymorphism in python
# https://www.codecademy.com/courses/python-for-programmers/articles/polymorphism-python

class Checking:
    def type(self):
        print('You have a checking account at the CA bank.')

    def balance(self):
        print('$25 in your checking.')

class Savings:
    def type(self):
        print('You have a saving account at the CA bank.')

    def balance(self):
        print('$2000 in your savings.')

account_a = Checking()
account_b = Savings()

for account in (account_a, account_b):
    account.type()
    account.balance()