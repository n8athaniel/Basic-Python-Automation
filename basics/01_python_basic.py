"""
    Part 1: Python Basics - Variables, Types, Control Flow
"""

# Variables & Data types
x = 5
name = "Nate"
pi = 3.14
is_ready = True 

# List & Loops
nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n)

# List Comprehension 
squares = [n**2 for n in nums]
print(squares)

# If/Else
x = 10
if x > 5:
    print ("Big")
elif x == 5:
    print("Equal")
else:
    print("Small")

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Nate"))
print(greet("Nathaniel"))

# Dictionaries 
user = {"name": "Nate", "age":22}
print(user["name"])

# Loop over dict 
for key, val in user.items():
    print(key, val)

""" 
    Tasks - part 1 
"""
# Create a list of numbers 1-5 and print the square of each 
# number using a for loop.
nums = [1, 2, 3, 4, 5]

for i in nums:
    print (f"The square of {i} is...", i**2)

# Write a function is_even(n) that returns True if the number is even.
def is_even(n):
    if n % 2 == 0:
        return(f"{n} is even")
    else:
        return(f"{n} is odd")

print(is_even(0))
print(is_even(1))
print(is_even(2))

# Given a dictionary of usernames and passwords, print each user 
# and mask their password (e.g. ****).
users = {"alice": "1234", "bob": "qwerty"}
for user, pw in users.items():
    print(f"{user}: {'*' * len(pw)}")