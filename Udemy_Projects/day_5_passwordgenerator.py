# DAY 5 - PASSWORD GENERATOR
# Run: python .\Udemy_Projects\day_5_passwordgenerator.py
# Related: Udemy_Projects\ (no helper files yet)

import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91
password_characters = []

for _ in range(nr_letters):
    password_characters.append(random.choice(letters))

for _ in range(nr_symbols):
    password_characters.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_characters.append(random.choice(numbers))

choice = int(
    input("Would you like your password's order randomized? Type 0 for no, 1 for yes.\n")
)

if choice == 1:
    random.shuffle(password_characters)

password = "".join(password_characters)
print(f"Your password is: {password}")
