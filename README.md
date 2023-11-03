# Python

- To enter python mode in the terminal (once python is installed) simply type `python` and you will be in python mode.
  - **To exit python mode type `exit()`**
    **Example of Basic Python Code**

```python
name = input('Please enter your name:')
print('Hello,', name)
file = open('name.md', mode='w')
file.write(name)
file.close()
file = open('name.md', mode='r')
file.read()
```

**REPL** - Read, Evaluate, Print, Loop

- The command line interface we get when we type `python3` or `python` in the terminal is a REPL.
- A blockchain chain is a list (which is a more complex data type than the following basic data types)

### Basic Data Types:

- Number: Can be an integer (whole number) or a float (decimal number)
- String: Just text.
- Boolean: Can be true or false
  **We also have complex data types like dictonaries and objects (which we will go into detail on later)**

### Variables:

- A variable is like an address for a value.
  > i.e. `name = 'Bryan'` is a variable that holds the value of 'Bryan'

```py
name = 'bryan'
print(name)
name = 'john'
print(name)
age = 27
print(age)
isOld = True
print(isOld)
```

#### Numbers

> The following code will cause an error (because age is a string and 1 is a number):

```py
age = '27'
print(age + 1)
```

- The following code will concatinate the strings:

```py
age = '27'
print(age + '1')
```

- The int function will turn any other type of data into a number:

```py
age = '27'
print(int(age) + 1)
# 28
```

- The int function will not work on something that cannot be converted to a number like the word `'hello'`.
  \*\*It is worth noting that in python you can add underscores to long numbers (where commas would normally go) to make them easier to read.
  > i.e.
  > `1_000_000` > **Strings**
- In python a string can be created using quotes or double quotes and if you want to preserve line breaks you can use tripple double quotes.

```py
text = "I'm pretty cool"
print(text)
escapedText = 'I\'m an escaped single quote.'
print(escapedText)
long_text = """
Python is a high-level, interpreted programming language
known for its clear syntax and readability,
making it an excellent choice for beginners and experts alike.
Designed by Guido van Rossum and first released in 1991,
Python's philosophy emphasizes code readability and a syntax that
allows programmers to express concepts in fewer lines of code.
It supports multiple programming paradigms, including procedural,
object-oriented, and functional programming.
Python's comprehensive standard library, dynamic typing,
and dynamic memory allocation make it suitable for a variety of applications,
 from web development to scientific computing.
"""
print(long_text)
```

### A list in python is created using square brackets `[]`, in other languages you may know it as an array.

> Working with lists:

```py
# Our values are going to be the amount of coins we're sending with transactions.
blockchain = [1,8.6,5.1]
print(blockchain)
print(blockchain[1])
addTwo = blockchain[1] + 2
print(addTwo)
#-------------------Adding Elements to List--------------------
# You could add an element by reassigning the blockchain variable...
blockchain = [1,8.6,5.1,10]
print(blockchain)
blockchain.append(3)
print('appended:',blockchain)
last_element = blockchain.pop()
print(last_element)
print('after pop:',blockchain)
## OUTPUT:
# [1, 8.6, 5.1]
# 8.6
# 10.6
# [1, 8.6, 5.1, 10]
# appended: [1, 8.6, 5.1, 10, 3]
# 3
# after pop: [1, 8.6, 5.1, 10]
```

## **The blockchain we are building will be composed of blocks which will be lists that store the current value and all previous values**

## Functions:

- In python the format is `def functionName():`
- In python you don't use semicolones at the end of a line and you use indentation instead of curly braces.

```py
def add_numbers(a, b):
    result = a + b
    print(result)
    return result
# Now you can call this function
result = add_numbers(3, 5)
print(result)  # This will print 8
```

---

### Blockchain Theory: Understanding Blocks

**What's a Block?**

- Of course a "Blockchain" consists of multiple "Blocks" - and a single Block simply can be considered a **data storage/container.** You can store **ANY data** of your choice in a Block.


- Cryptocurrencies like Bitcoin are the most prominent use-case of the Blockchain technology but you can also store simple text in Blocks if you want to. Of course using a Blockchain makes most sense for data that should be **secure and distributed** across a broad network though. Data transparencyand safety are key advantages of the Blockchain.
Even when considering Cryptocurrencies, **you don't actually store the coins** in a Block but rather the **transactions between users**. Atransaction then includes an amount of coins that should be transferred.
For the purposes of this project, the Blocks we start with only hold **a number**. So you can think of it as a transaction, though the sender and recipient is missing. But that's something which will be added once we had a look at more complex data structures than simple lists.
Multiple Blocks in a list of Blocks then formthe first simple Blockchain.
**Most basic blockchain list representation**

```py
blockchain = [[1]]
def add_value():
    blockchain.append([blockchain[-1],5.3])
    print(blockchain)
add_value()
add_value()
add_value()
# [[1], [[1], 5.3]]
# [[1], [[1], 5.3], [[[1], 5.3], 5.3]]
# [[1], [[1], 5.3], [[[1], 5.3], 5.3], [[[[1], 5.3], 5.3], 5.3]]
```
