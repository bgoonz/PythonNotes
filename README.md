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

`1_000_000`

**Strings**

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

**The blockchain we are building will be composed of blocks which will be lists that store the current value and all previous values**


