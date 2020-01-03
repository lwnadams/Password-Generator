import random
char_count = int(input("Enter number of characters for password: "))
i = 0
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = ""
while i != char_count:
    c = random.choice(s)
    if c not in password:
        password = password + c
        i = i + 1
print(i)



print(password)