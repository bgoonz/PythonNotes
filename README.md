# Python

### Useful Resources & Links

- More on Python Basics: [https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- More on Python Functions: [https://docs.python.org/3/tutorial/controlflow.html#defining-functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- Python Floating Point Precision: [https://docs.python.org/3/tutorial/floatingpoint.html](https://docs.python.org/3/tutorial/floatingpoint.html)
- PEBs: [https://www.python.org/dev/peps/](https://www.python.org/dev/peps/)
- PEB 8 - Style Guide: [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
- String Escape Characters: [http://python-reference.readthedocs.io/en/latest/docs/str/escapes.html](http://python-reference.readthedocs.io/en/latest/docs/str/escapes.html)
- Example Docstrings: [http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- More on the Python Extension for Visual Studio Code: [https://code.visualstudio.com/docs/languages/python](https://code.visualstudio.com/docs/languages/python)

* To enter python mode in the terminal (once python is installed) simply type `python` and you will be in python mode.
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

- Even when considering Cryptocurrencies, **you don't actually store the coins** in a Block but rather the **transactions between users**. Atransaction then includes an amount of coins that should be transferred.

- For the purposes of this project, the Blocks we start with only hold **a number**. So you can think of it as a transaction, though the sender and recipient is missing. But that's something which will be added once we had a look at more complex data structures than simple lists.

- Multiple Blocks in a list of Blocks then formthe first simple Blockchain.

**Most basic blockchain list representation**

```py
blockchain = [[1]]


def add_value(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print(blockchain)


add_value(6.9)
add_value(420)
add_value(711)

# [[1], [[1], 6.9]]
# [[1], [[1], 6.9], [[[1], 6.9], 420]]
# [[1], [[1], 6.9], [[[1], 6.9], 420], [[[[1], 6.9], 420], 711]]
```

**Default Arguments**

- default arguments allow you to specify default values for parameters in a function. When you call the function and don't provide a value for a parameter with a default argument, the default value is used instead. This can be helpful when you want to make a function more flexible by allowing some parameters to be optional.

```py
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling the function with both arguments
greet("Alice", "Hi")  # Output: Hi, Alice!

# Calling the function with only one argument (uses the default greeting)
greet("Bob")           # Output: Hello, Bob!

```

**Using Default Arguments in Blockchain Example**

```py
blockchain = []
def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

add_value(6.9)
add_value(420,get_last_blockchain_value())
add_value(711,get_last_blockchain_value())

print(blockchain)
```

#### Keyword Arguments

in Python are a way to pass arguments to a function using the name of the parameter regardless of their order in the parameter list. This can make the code more readable and clear, especially when a function has a lot of parameters or when you are passing literals that might be unclear on their own.

When defining a function, you simply give each parameter a name. When calling the function, you use the syntax `parameter_name=value` to indicate which argument goes with which parameter.

```py
# Function definition with two parameters
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Calling function with keyword arguments
greet(first_name="John", last_name="Doe")
greet(last_name="Doe", first_name="John")  # The order of named arguments can be changed
# Both calls to greet will output Hello, John Doe!, because we're specifying which argument goes with which parameter by name, so the order doesn't matter.
```

> Another example:

```py
# Function definition with default values for parameters
def describe_pet(animal_type='dog', pet_name='Rex'):
    print(f"I have a {animal_type} named {pet_name}.")

# Calling function with no arguments uses the default values
describe_pet()
# Output: I have a dog named Rex.

# Calling function with one positional argument overrides the first default value
describe_pet('hamster')
# Output: I have a hamster named Rex.

# Calling function with one keyword argument only overrides the specified parameter
describe_pet(pet_name='Hamlet')
# Output: I have a dog named Hamlet.

# Calling function with both keyword arguments
describe_pet(animal_type='parrot', pet_name='Polly')
# Output: I have a parrot named Polly.
```

---

### Variable Scope:

- In python we have `global` and `local` scope.
- Global variables are defined at the top level of a python file and can be used anywhere in the code within that file after the line where the varialbe is defined.
- Local variables are only available inside of a function (function arguments or variables defined in the function)

> Example:

```py
blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    user_input= float(input('Transaction amount?  '))
    return user_input
```

- In the code above, blockchain is a global variable while user_input is a local variable
- Furtherm as arguments to add_value... transaction_amount and last_transaction are variables that are local to the add_value function.

---

---

## Loops & Conditional Code:

- Python has two types of loops, `for loops`, and `while loops`.

  - For Loop:
    - In Python, a for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or any other iterable object. Here's a simple example that iterates over a list of numbers and prints each number:

        ```py
        numbers = [1, 2, 3, 4, 5]
        for number in numbers:
            print(number)
        ```


    - While Loop:
      - A `while` loop in Python repeatedly executes a block of code as long as a given condition is true. Here's a simple example that uses a `while` loop to count down from 5 to 1:

        ```py
        count = 5
        while count > 0:
            print(count)
            count -= 1  
        ```

**The difference**
- A for loop allows you to iterate through the elements of an iterable (e.g a list).. A while loop allows you to repeat code as long as it's condition is True.

    - In a For loop you should not modify the iterable in the loop block or you could either end up skipping elements or inserting them infinately.
    - For While loops you should provide an exit condition (otherwise you will need to ctrl +Z out of the loop).


**Using both in our blockchain example**

```py
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
    add_value(
        last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount
    )
    for block in blockchain:
        print("Outputting block")
        print(block)

```

---

### Conditionals:

```py
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
    else:
        print_blockchain_elements()
```
