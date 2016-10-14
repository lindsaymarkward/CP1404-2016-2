"""
Challenge:
Using the with statement, read a file and print the last line in it
"""
from cart import Cart

Cart()

with open('data.csv') as f:
    lines = f.readlines()
print(lines[-1])

