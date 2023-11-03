# Our values are going to be the amount of coins we're sending with transactions.
blockchain = [1, 8.6, 5.1]
print(blockchain)
print(blockchain[1])

addTwo = blockchain[1] + 2
print(addTwo)

# -------------------Adding Elements to List--------------------
# You could add an element by reassigning the blockchain variable...
blockchain = [1, 8.6, 5.1, 10]
print(blockchain)


blockchain.append(3)
print("appended:", blockchain)

last_element = blockchain.pop()
print(last_element)
print("after pop:", blockchain)
