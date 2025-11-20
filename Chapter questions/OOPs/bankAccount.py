

class BankAccount:
    def __init__(self, name, account_number, email, balance):
        self.name = name
        self.__account_number = account_number
        self.__email = email
        self.__balance = balance
    

    def set_account_number(self, new_account_number):
        self.__account_number = new_account_number

    def get_account_number(self):
        return self.__account_number
    
    def set_email(self, new_email):
        self.__email = new_email

    def get_email(self):
        return self.__email

    def set_balance(self, new_balance):
        if new_balance < 0:
            return "The balance cannot be negative"
        self.__balance = new_balance

    def get_balance(self):
        return self.__balance


def main():
    name = "Alice"
    account_number = "987654321"
    email = "alice@example.com"
    balance = 1500
    new_account_number = "1234567890"
    new_email = "alice_new@example.com"
    new_balance = 3000 

    account = BankAccount(name, account_number, email, balance)

    account.set_email(new_email)
    print(account.get_email())

    account.set_account_number(new_account_number)
    print(account.get_account_number())

    error_message = account.set_balance(new_balance)

    if error_message:
        print(error_message)
    else:
        print(account.get_balance())
main()