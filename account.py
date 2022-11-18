class Account:
    '''
    creating a class for account with methods such as deposit, withdraw
    get_balance and get_name
    '''
    def __init__(self, name: str) -> None:
        '''
        initializing objects for account class
        :param name: This is the account name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        '''
        deposit or add specified amount to account balance
        :param amount: This is the deposited amount
        :return: if deposit successful returns True, if unsuccessful returns False
        '''
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        '''
        withdraw method to withdraw specified amount from account balance
        :param amount: this is the withdrawn amount
        :return: if withdraw successful returns True, if unsuccessful returns False
        '''
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance = self.__account_balance - amount
                return True
            else:
                return False
        else:
            return False

    def get_balance(self) -> float:
        '''
        method to get the private variable __account_balance bank balance
        :return: balance of account
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        method to get the private variable __account_name bank holder name
        :return: name of account holder
        '''
        return self.__account_name