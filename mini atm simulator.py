# Mini ATM Simulator

balance = 1000.00
PIN = "7985"


def verification():
    # Ask user to input pin for verification
    while True:
        entered_pin = input("Enter your pin ")
        if entered_pin == PIN:
            return True
        else:
            print("Incorrect pin. Try again")


def check_balance():
    print(f"Your current balance is: ${balance:.2f}\n")


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"${amount:.2f} deposited successfully!")
        check_balance()
    else:
        print("Invalid deposit amount.\n")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.\n")
    elif amount <= 0:
        print("Invalid withdrawal amount.\n")
    else:
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully!")
        check_balance()


def atm_menu():
    if verification():
        while True:
            print("ATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                check_balance()
            elif choice == "2":
                deposit()
            elif choice == "3":
                withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.\n")


# Run the ATM
atm_menu()
