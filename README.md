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

- The int function will not work on something that cannot be converted to a number  like the word `'hello'`.


**It is worth noting that in python you can add underscores to long numbers (where commas would normally go) to make them easier to read.

>i.e.

`1_000_000`

