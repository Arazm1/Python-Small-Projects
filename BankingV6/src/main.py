import mysql.connector

class BankingProgram:
    def __init__(self, db_config):
        self.account = BankAccount(db_config)

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
                self.account.get_balance()
            elif choice == "2":
                amount = float(input("Enter an amount to be deposited: "))
                self.account.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter amount to be withdrawn: "))
                self.account.withdraw(amount)
            elif choice == "4":
                print("Thank you for using the Banking program! Have a nice day!")
                is_running = False
                self.account.close_connection()
            else:
                print("That is not a valid choice!")




class BankAccount:
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor(dictionary=True)

    def get_balance(self):
        sql = "SELECT balance FROM bankacc WHERE id = 1"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:
            print(f"Balance: {result['balance']}")
            return result['balance']
        else:
            print("No balance found.")
            return None

    def deposit(self, amount):
        sql = "UPDATE bankacc SET balance = balance + %s WHERE id = 1"
        self.cursor.execute(sql, (amount,))
        self.connection.commit()
        print(f"Deposited {amount}. New balance:")
        self.get_balance()

    def withdraw(self, amount):
        sql = "UPDATE bankacc SET balance = balance - %s WHERE id = 1"
        self.cursor.execute(sql, (amount,))
        self.connection.commit()
        print(f"Withdrew {amount}. New balance:")
        self.get_balance()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


db_config = {
    'host': 'localhost',
    'port': 3306,
    'database': '',     #Your database name
    'user': '',         #Your username   
    'password': '',     #Your password
    'autocommit': True
}

if __name__ == "__main__":
    program = BankingProgram(db_config)
    program.run()