# Write a Python program that takes an integer
# input from the user and checks if it is an Armstrong number (a number that is
# equal to the sum of its own digits raised to the power of the number of digits)
# using a for loop.

number = int(input("Enter an integer: "))

num_str = str(number)
num_digits = len(num_str)

sum_of_powers = 0

for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

if sum_of_powers == number:
    print(str(number) +" is an Armstrong number.")
else:
    print(str(number) +" is not an Armstrong number.")