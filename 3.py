# Task 3
# Create a simple ATM simulation. The program should allow the user to:
#
# Check their balance.
# Deposit money.
# Withdraw money (ensure there’s enough balance). The user can perform multiple operations until they choose to exit.

balance = 500
is_finished = False

while not is_finished:
    operation_type = int()

    try:
        operation_type = int(
            input("choose operation, enter 0 for check balance, 1 for deposit money, 2 for withdraw money: "))

        if operation_type in (0, 1, 2):
            if operation_type == 0:
                print(f'your balance is {balance}')
            if operation_type == 1:
                value = int(
                    input("enter how much you want to deposit: "))

                balance += value
                print("Success")
            if operation_type == 2:
                value = int(
                    input("enter how much you want to withdraw: "))

                if balance < value:
                    print("not enough money to withdraw")
                else:
                    balance -= value
                    print("Success")
        else:
            print("Choose correct option.")

    except:
        print("not a number")
        is_finished = True
