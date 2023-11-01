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
> The following code will cause an error:

```py
age = '27'
print(age + 1)
```
