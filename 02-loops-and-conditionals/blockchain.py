blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input("Transaction amount?  "))
    return user_input


def get_user_chocie():
    user_input = input("Your choice:")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print("Outputting block")
        print(block)


tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    user_choice = get_user_chocie()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_value(
            last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount
        )
    elif user_choice == '2':
        print_blockchain_elements()
    else:
        print('Input is invalid! please enter a number from the list of options')
