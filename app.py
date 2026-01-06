print("===== WELCOME TO ATM =====")

balance = 5000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    print("PIN verified successfully")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance = balance - amount
            print("Please collect your cash")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 3:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Amount deposited successfully")
        print("Updated balance:", balance)

    else:
        print("Invalid option")

else:
    print("Incorrect PIN")

print("Thank you for using ATM")
