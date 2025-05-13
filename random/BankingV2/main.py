class BankAccount:
    def __init__(self):
        self.balance = 0

    def show_balance(self):
        print(f"Your balance is ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("That's not a valid amount")
        else:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Amount must be greater than zero")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}")


class BankingProgram:
    def __init__(self):
        self.account = BankAccount()

    def run(self):
        is_running = True
        while is_running:
            print("__---______---__")
            print("Banking Program")
            print("----------------")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.account.show_balance()
            elif choice == "2":
                amount = float(input("Enter an amount to be deposited: "))
                self.account.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter amount to be withdrawn: "))
                self.account.withdraw(amount)
            elif choice == "4":
                print("Thank you for using the Banking program! Have a nice day!")
                is_running = False
            else:
                print("That is not a valid choice!")



program = BankingProgram()
program.run()
