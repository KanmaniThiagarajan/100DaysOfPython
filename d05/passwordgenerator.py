# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letter="" #to save the letters from the letters list eg. nr_letters=4 , letter=abcd
for l in range(0,nr_letters): #if nr_letters=3, loop will iterate 3 times add the letters like a,ab,abc
    result=random.choice(letters)
    letter+=result

symbol="" #to save the symbol from the symbols list eg. nr_symbols=2 , symbol=!$
for s in range(0,nr_symbols): #if nr_symbols=3, loop will iterate 3 times and concat the symbol like !,!#,!#$
    result=random.choice(symbols)
    symbol+=result

number="" #to save the number from the numbers list eg. nr_numbers=3 , number=123
for s in range(0,nr_numbers): # if nr_numbers=3, loop will iterate 3 times and concat number like a 1,12,123
    result=random.choice(numbers)
    number+=result 

result=letter+number+symbol #the password shoul be the combination of letters, symbols and numbers hence its concatenated
password_list=list(result) #converting the result to list as shuffle function works with only list
print(password_list) #list before shuffling
random.shuffle(password_list) #the characters in the list will be shuffled now
print(password_list) #list after shuffling
password="" 
for char in password_list: #for every characters (char) in the list (shuffled list), we will be putting them together as a bunch of characters instead of list
     password+=char 
print(password)