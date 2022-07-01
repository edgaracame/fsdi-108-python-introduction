# single line comment
# another line

# variables
name = "Edgar"
last_name = 'Antonio'
age = 23
price = 12.33
found = False
valid = True

# display
print("Hi there, my name is " + name + " and I am " + str(age) + " years old")

# conditions
if(age < 100):
    print("No worries, you are still young!")
elif age == 100:
    print("Wow, you reached the century!")
else:
    print("Sorry, you are getting a little old now!")

# functions


def hello():
    print("Line 1")
    print("Line 2")
    print("Line 3")


def say_hello():
    print("Hello there:")


print("Line 4")

hello()
say_hello()
