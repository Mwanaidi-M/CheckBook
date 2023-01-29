import os
import re


def menu():
    """
Function that displays the introductory welcome message and menu options for the
checkbook program.
    """
    welcome_msg = " WELCOME TO THE CHECKBOOK "
    print(f"{welcome_msg:-^100}")
    print("""
1. CREATE ACCOUNT
2. DEPOSIT TO ACCOUNT
3. WITHDRAW FROM ACCOUNT
4. VIEW BALANCE
5. EXIT
    """)


def create_account(acc_name):
    """
Function that creates a user account in form of a .txt file and initializes their balance to 0.0.
Before creating the account, check if the account already exists; if it does then inform the user
of that else, create the account and let them know the account was created successfully.

:param acc_name: <str>
    """
    user_acc = os.path.join(os.getcwd(), f"{acc_name}.txt")
    initial_bal = float(0)

    if os.path.exists(user_acc):
        print("Account already exists.")
    else:
        with open(f"{acc_name}.txt", 'w') as new_user_acc:
            new_user_acc.write(str(initial_bal))

        print(f"\nAccount: {acc_name} created successfully.")
        print(f"Balance: {initial_bal}\n")


def deposit(acc_name, amount):
    """
Function that enables the user to deposit an amount to their account.

Check if the account name given exists, if it does then open the account file to view
the current balance and add it to the amount the user provides then update the account
file with the new amount.

:param acc_name: <str>
:param amount: <int> or <float>
    """
    user_acc = os.path.join(os.getcwd(), f"{acc_name}.txt")
    if not os.path.exists(user_acc):
        print("\nAccount does not exist.")
    else:
        with open(f"{acc_name}.txt") as view_acc:
            curr_bal = float(view_acc.read())

        with open(f"{acc_name}.txt", 'w') as account:
            new_bal = curr_bal + amount
            account.write(str(new_bal))

        with open(f"{acc_name}.txt") as check_acc:
            acc_bal = check_acc.read()
        print(f"\nbalance: {float(acc_bal)}")


def withdraw(acc_name, amount):
    """
Function that enables the user to withdraw an amount from their account.

Check if the account name given exists, if it does then open the account file to view
the current balance.

Check if the current balance is greater than the amount the user wants to withdraw and subtract
the given amount from the current balance then update the account file with the new amount.

If the amount is greater than the current account balance, let user know they have insufficient funds.

:param acc_name: <str>
:param amount: <int> or <float>
    """
    user_acc = os.path.join(os.getcwd(), f"{acc_name}.txt")
    if not os.path.exists(user_acc):
        print("\nAccount does not exist.")
    else:
        with open(f"{acc_name}.txt") as view_acc:
            curr_bal = float(view_acc.read())
            if curr_bal < amount:
                print("\nInsufficient funds to make withdrawal.")
            else:
                with open(f"{acc_name}.txt", 'w') as account:
                    new_bal = curr_bal - amount
                    account.write(str(new_bal))

                with open(f"{acc_name}.txt") as check_acc:
                    acc_bal = check_acc.read()
                print(f"\nbalance: {float(acc_bal)}")


def view_balance(acc_name):
    """
Function that displays the current account balance of a given user account name.

:param acc_name: <str>
    """
    user_acc = os.path.join(os.getcwd(), f"{acc_name}.txt")

    if not os.path.exists(user_acc):
        print("\nAccount does not exist")
    else:
        with open(f"{acc_name}.txt") as acc_view:
            acc_bal = acc_view.read()
        print(f"\nbalance: {float(acc_bal)}")


def validate_account_name():
    """
Function that checks if a given name matches a certain pattern and returns the name if it does.
The name can only contain lowercase and uppercase letters, numbers, ()_-,. characters;
the name must have at least one character.

:return: user_acc <str>
    """
    user_acc = input("Enter your account name: \t")
    acc_pattern = re.compile(r"^[a-zA-Z0-9()_\-,.]+$")
    if re.search(acc_pattern, user_acc) is None:
        print(r"""
Account name cannot contain any space character or any of the following characters:
@ $ % & \ / : * ? " ' < > | ~ ` # ^ + = { } [ ] ; !
        """)
    else:
        return user_acc


def validate_amount():
    """
Function that returns the amount if:
- The amount is greater than 0 and less than 1_000_000.
- It matches the given pattern ie
    * a number beginning with values in the range [1-9] followed by 0 or more digits.
    * a number beginning with values in the range [1-9] followed by 0 or more digits and
        has 2 digits rounded after the decimal point.

:return: amount <float>
    """
    try:
        amount = float(input("Enter amount:\t"))
    except Exception as exc:
        print("\nInvalid amount input.")
    else:
        amount_pattern = re.compile(r"^([1-9]\d*)$|^([1-9]\d*\.\d{,2})$")

        if amount <= 0 or amount >= 1_000_000:
            print("\nAmount must be between 1 and 999_999")
        elif re.search(amount_pattern, str(amount)) is None:
            print("""
    A valid amount:
    - must be a whole number
    - contain only digits (0 – 9) 
    - can only have 2 digits rounded after the decimal point.
            """)
        else:
            return amount
