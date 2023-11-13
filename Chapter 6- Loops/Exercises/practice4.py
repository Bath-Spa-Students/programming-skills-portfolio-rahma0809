#. Write a Python program that uses the break statement to exit a for loop when a specific condition is met
numbers= [15, 28, 9, 12, 6, 27, ]
for num in numbers:
    if num%3==0:
        print(f'Multiples of 3:{num}')
        break