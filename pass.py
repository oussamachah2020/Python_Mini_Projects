import random as rm

password_length = int(input("Enter the password length: "))
characters = 'abcdefghijklmnopqrstuvwxyz1234567890/;#:$*^"[]{}'

password = "".join(rm.sample(characters, password_length))
print(password)