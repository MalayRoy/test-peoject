# Write a Python program that prints the numbers from 1 to 100. But for
# multiples of three, print "Fizz" instead of the number, and for the multiples of five,
# print "Buzz". For numbers that are multiples of both three and five, print
# "FizzBuzz" using a for loop.

for number in range(1, 101):  # Loop from 1 to 100
    if number % 3 == 0 and number % 5 == 0:  # Multiples of both 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:  # Multiples of 3
        print("Fizz")
    elif number % 5 == 0:  # Multiples of 5
        print("Buzz")
    else:  # For all other numbers
        print(number)