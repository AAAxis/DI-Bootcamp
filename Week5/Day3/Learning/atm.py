from typing import Union

class AtmAccount:

    available_account = 9991

    def __init__(self, holder) -> object:
        self.__balance = 0.0 #  _ protected
        self.__holder = holder  # __ private
        self.__account_number = AtmAccount.available_account
        AtmAccount.available_account += 1

    @property
    def funds(self) -> float:
        return self.__balance

    @funds.setter
    def _funds(self, amount: Union[int, float]) -> None:
        self.__balance = amount

    def deposit(self, amount: Union[int, float]) -> None:
        self._funds += amount

    def withdraw(self, amount: Union[int, float]) -> None:
        if amount > self.funds:
            raise ValueError("Insufficient funds")
        self._funds -= amount

    def __str__(self) -> str:
        output = f"""
        Account number: {self.__account_number}
        Holder: {self.__holder}

        Balance: {self.funds}
        """
        return output


    def __repr__(self) -> str:
        return str(self.__dict__)

    def __iadd__(self, amount):  # __iadd__ == +=
        self.deposit(amount)
        return self

    def __isub__(self, amount): # __isub__ == -=
        self.withdraw(amount)
        return self

    


account1 = AtmAccount('Yossi Eik')

account1.deposit(100)
account1.withdraw(100)
account1 += 100
account1 -= 50
print(account1)

print(repr(account1))

