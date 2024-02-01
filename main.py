import random
import datetime
accounts = []

class Account:
    def __init__(self, name, accType, createDate, balance, accNumber):
        self.name = name
        self.type = accType
        self.createDate = createDate
        self.balance = balance
        self.number = accNumber

def createAcc(accNumber, balance):
    name = input('Please enter a name: ')
    accType = input('Please enter an account type: ')
    creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    newAcc = Account(name, accType, creation_date, balance, accNumber)
    accounts.append(newAcc)
    print('The account has been added successfully! The Account information: ','\n')
    print('\n', newAcc.name, '\n', newAcc.type, '\n', newAcc.createDate, '\n', newAcc.balance, '\n', newAcc.number)

def display():
    for match in accounts:
        print('\n', match.name, '\n', match.type, '\n', match.createDate, '\n', match.balance, '\n',match.number)

def update(accNumber):
    for i in range(len(accounts)):
        match = accounts[i]
        if match.number == accNumber:
            accounts.remove(match)
            name = input('Please enter a name: ')
            accType = input('Please enter an account type: ')
            creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            newAcc = Account(name, accType, creation_date, balance, accNumber)
            accounts.append(newAcc)
            print('The account has been added successfully! The Account information: ', '\n')
            print('\n', newAcc.name, '\n', newAcc.type, '\n', newAcc.createDate, '\n', newAcc.balance, '\n',
                  newAcc.number)

        else:
            print('No account found.')

def delete(accNumber):
    for i in range(len(accounts)):
        match = accounts[i]
        if match.number == accNumber:
            accounts.remove(match)
            print('The account has been deleted')
        else:
            print('No account found.')

def search(accNumber):
    for i in range(len(accounts)):
        match = accounts[i]
        if match.number == accNumber:
                print('The Account information: ')
                print('\n',match.name, '\n', match.type, '\n', match.createDate, '\n', match.balance, '\n',
                      match.number)
        else:
            print('No account found.')

def deposit(accNumber, balance):
    for i in range(len(accounts)):
        match = accounts[i]
        if match.number == accNumber:
                value = match.balance
                value += balance
                match.balance = value
                print('The current balance is: ', match.balance)
        else:
            print('No account found.')

def withdraw(accNumber, balance):
    for i in range(len(accounts)):
        match = accounts[i]
        if match.number == accNumber:
                value = match.balance
                value -= balance
                if value < 10 :
                    print('The amount cannot be withdrawn. It exceeds the minimum balance of 10$ or you withdrawn more than balance.')
                else:
                    match.balance = value
                    print('The current balance is: ', match.balance)
        else:
            print('No account found.')

while True:
    print("\nMenu:")
    print("1. Create a new account")
    print("2. Display all accounts")
    print("3. Update an account")
    print("4. Delete an account")
    print("5. Deposit an amount into your account")
    print("6. Withdraw an amount from your account")
    print("7. Search for an account")
    print("8. Exit")

    console_input = int(input('Please choose an input from 1 to 8: '))

    if 1 <= console_input <= 8:
        if console_input == 1:
            accNumber = random.randint(0, 1000000000)
            amount = int(input('The minimum amount to withdraw is 10$.Please enter an amount: '))
            while amount < 10:
                print('Please try again.')
                amount = int(input('The minimum amount to withdraw is 10$.Please enter an amount: '))
            createAcc(accNumber, amount)
        elif console_input == 2:
            display()
        elif console_input == 3:
            accNumber = int(input('Please enter the account number: '))
            update(accNumber)
        elif console_input == 4:
            accNumber = int(input('Please enter the account number: '))
            delete(accNumber)
        elif console_input == 5:
            balance = int(input('Please enter a deposit amount: '))
            number = int(input('Please enter the account number: '))
            deposit(number, balance)
        elif console_input == 6:
            amount = int(input('The minimum balance is 10$.Please enter an amount: '))
            number = int(input('Please enter the account number: '))
            withdraw(number, amount)
        elif console_input == 7:
            accNumber = int(input('Please enter the account number: '))
            search(accNumber)
        else:
            print('Exit')
            break
    else:
        print('Please choose a number from 1 to 8.')
