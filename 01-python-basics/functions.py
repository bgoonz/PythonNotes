def add_numbers(a, b):
    result = a + b
    print(a, "+", b, "=", result)
    return result


# Now you can call this function
result = add_numbers(3, 5)
print(result)  # This will print 8


#----------Default Arguments:------------------

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling the function with both arguments
greet("Alice", "Hi")  # Output: Hi, Alice!

# Calling the function with only one argument (uses the default greeting)
greet("Bob")           # Output: Hello, Bob!

