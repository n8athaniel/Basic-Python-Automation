""" 
    Part 2: List Comprehensions & String Manipulation 
"""

# List Comprehenstions 
nums = [1, 2, 3, 4, 5, 6]
squares = [n**2 for n in nums if n % 2 == 0]
print(squares) #squares of even numbers only  

# String Manuipulation Basic 
s = "hello world"

print(s.upper())                     # HELLO WORLD
print(s.capitalize)                  # Hello world
print(s.replace("hello", "Yo"))      #Yo world
print(s.split())                     # ['hello'], ['world']
print("-".join(['hello', 'Python'])) # hello-Python

# Check substring
print("world" in s)                  # True

# F-strings (formatted strings)
name = "Nate"
age = 22
print(f"My name is {name} and I am {age} years old.")

""" 
    Tasks - part 2 
"""

# Using list comprehension, create a list of the cubes of numbers 1-10 
# that are divisible by 3.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cubes = [n**3 for n in nums if n % 3 == 0]
print(cubes)


# Given the string "Automation is fun!", replace "fun" with "powerful" 
# and print it in uppercase.
assertion = "Automation is fun!"
print(assertion.replace("fun", "powerful").upper())

# Write a function greet_person(name, age) that returns 
# "Hello {name}, you are {age} years old." using f-strings.
def greet_person(name, age):
    return(f"Hello {name}, you are {age} years old.")

print(greet_person("Nathaniel", 22))