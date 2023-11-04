# Create two variables... one with your name and one with your age.
# Create a function that prints your data as one string.
# Create a function which prints ANY data (2 arguments) as one string.
# Create a function which calculates and returns the numer of decades you have been alive.

my_name = input("what is your name? ")
my_age = int(input("What is your age? "))


def my_data(name=my_name, age=my_age):
    print(f"{name} : {age}")


my_data()


def decades(age=my_age):
    divide_by_10 = age / 10
    decades_alive = int(divide_by_10)
    return decades_alive


print(decades())
