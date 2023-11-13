'''Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop.'''

largest_number = float('-inf') 

while True:
    user_input = input("Enter a number (enter '0' to exit): ")

    if user_input == '0':
        break

    number = float(user_input)

    if number > largest_number:
        largest_number = number

print("The largest number entered is:", largest_number)
