import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to Python.password generator")
nr_letters = int(input("How many letters do you want in your password?\n"))
nr_numbers = int(input("How many numbers do you want in your password?\n"))
nr_symbols = int(input("How many symbols do you want in your password?\n"))
password = []
for letter in range(nr_letters):
    password+= random.choice(letters)
for number in range(nr_numbers):
    rann = random.choice(numbers)
    password+=rann
for symbol in range(nr_symbols):
    rans = random.choice(symbols)
    password+=rans
random.shuffle(password)
strlist =''.join(password)
print(strlist)
