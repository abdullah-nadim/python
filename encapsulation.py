class Bank:
    def __init__(self,name):
        self.name = name
        self.__balance= 10000

    def get_balance(self):
        return self.__balance

account = Bank("Tony")
print(account.name)
print(account.get_balance())
