#password generator
from random import randint
password=""

for i in range(8):
    password += chr(randint(32,126))
print(password)

