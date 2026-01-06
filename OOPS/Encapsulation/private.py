# Prefix with double underscore __ refers private members
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance   # private

acc = BankAccount(5000)

# To access private members _ClassName__variableName
# Not preferred..
# Private is not 100% locked
# Name mangling
print(acc._BankAccount__balance)  
