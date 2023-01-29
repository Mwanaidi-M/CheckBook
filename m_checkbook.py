from m_operations \
    import menu, create_account, deposit, withdraw, view_balance, validate_account_name, validate_amount
import time

"""
Write a rudimentary checkbook balancing program. It will read a line, which will contain either
the word "withdraw" or "deposit". The next line will contain the amount of the check or deposit.
After reading each pair of lines, the program should compute and print the new balance.

For example, given the input
deposit
100
withdraw
12.34
withdraw
49.00
deposit
7.01

the program should print something like
balance: 100.00
balance: 87.66
balance: 38.66
balance: 45.67
"""

while True:
    menu()
    try:
        user_input = int(input("ENTER THE NUMBER OF THE TASK YOU WISH TO PERFORM:\t"))
    except Exception as exc:
        print("\nInvalid Input.")
    else:
        if user_input not in range(1, 6):
            print("\nMenu option does not exist.")
        else:
            if user_input == 1:
                name_acc = validate_account_name()
                if name_acc is not None:
                    create_account(name_acc)
            elif user_input == 2:
                name_acc = validate_account_name()
                dep_amount = validate_amount()

                if name_acc is not None and dep_amount is not None:
                    deposit(name_acc, dep_amount)
            elif user_input == 3:
                name_acc = validate_account_name()
                with_amount = validate_amount()

                if name_acc is not None and with_amount is not None:
                    withdraw(name_acc, with_amount)

            elif user_input == 4:
                name_acc = validate_account_name()
                if name_acc is not None:
                    view_balance(name_acc)
            else:
                print("\nExiting Program...BYE")
                time.sleep(2)
                break
