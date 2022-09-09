from typing import Union

class AtmAccount:

    available_account = 9991

    def __init__(self, holder) -> object:
        self.__balance = 0.0 #  _ protected
        self.__holder = holder  # __ private
        self.__account_number = AtmAccount.available_account
        AtmAccount.available_account += 1

    def funds(self) -> float:
        return self.__balance

    def deposit(self, amount: Union[int, float]) -> None:
        self.__balance += amount

    def withdraw(self, amount: Union[int, float]) -> None:
        if amount > self.funds():
            raise ValueError("Insufficient funds")
        self.__balance -= amount



account1 = AtmAccount('Yossi Eik')

account1.deposit(100)
print(account1.funds())

account1.withdraw(100)
print(account1.funds())

