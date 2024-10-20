# Task 1: Input Length Validator 
# Write a script that asks for and checks the length of the user's first name and last name.
# Both should be at least 2 characters long. If not, print an error message.

def first_name_checker(first_name):
    first_name_length = len(first_name)
    return first_name_length

def last_name_checker(last_name):
    last_name_length = len(last_name)
    return last_name_length
 
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

first_name_total = first_name_checker(first_name)
if first_name_total >= 2:
    print(f"Your first name, {first_name}, is {first_name_total} characters long.")
else:
    print("Invalid entry. You must enter at least two letters.")

last_name_total = last_name_checker(last_name) 
if last_name_total >= 2:
    print(f"Your last name, {last_name}, is {last_name_total} characters long.")
else:
     print("Invalid entry. You must enter at least two letters. ")

