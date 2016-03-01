"""
.. module:: m2_decorator
    :synopsis: This is a class example for module 2

.. moduleauthor:: RickChung
"""

class Account(object):
    """
    Account is a class eample.
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0.0

    def deposit(self, amount):
        """
        deposit some amount of money to the account

        Return:
            int: the amount of money you deposit
        """
        self.balance += amount
        return amount

    def withdraw(self, amount):
        """
        withdraw some money from the account.

        Args:
            int: amount

        Return:
            int: money you want to withdraw

        Raises:
            ValueError if there is no enough balance

        >>> account.withdraw()
        """
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            raise ValueError('No enough balance')

    def __str__(self):
        return ('Account[id={id}, name={name}, balance={balance}]'
            .format(id=self.id, name=self.name, balance=self.balance))

class CheckingAccount(Account):
    """
    This is a CheckingAccount derived from Account class.
    """
    def __init__(self, id, name):
        super(CheckingAccount, self).__init__(id, name)     # Call constructor in the parent class
        self.overdrafitlimit = 30000

    def withdraw(self, amount):
        """
        passed amount cannot exceed the sum of balance and overdrafitlimit.

        Args:
            int: amount

        Return:
            int: amount

        """
        if amount <= self.balance + self.overdrafitlimit:
            self.balance -= amount
            return amount
        else:
            raise ValueError('You cannot withdraw so much')

    def __str__(self):
        return ('CheckingAccount[id={id}, name={name}, balance={balance}, overdrafitlimit={overdrafitlimit}]'
                .format(id=self.id, name=self.name, balance=self.balance, overdrafitlimit=self.overdrafitlimit))

if __name__ == '__main__':
    account = Account(1, 'my name')
    print(account.name)
    account.deposit(1000)
    print(account)
    print(account.withdraw(100))

    checkingAccount = CheckingAccount(2, 'my checking account')
    print(checkingAccount.name)
    checkingAccount.deposit(10000)
    print(checkingAccount)
    print(checkingAccount.withdraw(10))