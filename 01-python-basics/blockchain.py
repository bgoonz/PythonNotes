blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])
    


add_value(6.9)
add_value(420,get_last_blockchain_value())
add_value(711,get_last_blockchain_value())

print(blockchain)
