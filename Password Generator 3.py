#password generator v3
import random
cars = "abcdefghijklmnopqrstuvwyz"
password = random.choice(chars)

print(password)

password=""
length = input("What's the password length that you want")
for i in range(3):
for i in range(length):
    password += random.choice(chars)

print(password)

