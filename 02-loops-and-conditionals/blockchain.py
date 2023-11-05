blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    user_input = float(input("Transaction amount?  "))
    return user_input


tx_amount = get_user_input()
add_value(tx_amount)





while True:
    tx_amount = get_user_input()
    add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)
    for block in blockchain:
        print('Outputting block')
        print(block)
