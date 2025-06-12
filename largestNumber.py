# Largest among Three Numbers: Write a Python program that takes three
# numbers as input and prints out the largest among them.

number1 = int(input("Enter Number 1 : "))
number2 = int(input("Enter Number 2 : "))
number3 = int(input("Enter Number 3 : "))

if number1 > number2 and number1 > number3:
    print("Largest Number : " + str(number1 ))
elif number2 > number1 and number2 > number3:
    print("Largest Number : " + str(number2))
else:
    print("Largest Number : " + str(number3))