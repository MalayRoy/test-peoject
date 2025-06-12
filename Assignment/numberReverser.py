# Write a Python program that takes an integer input from the
# user and prints its reverse using a while loop.

number = int(input("Enter an integer: "))

reverse = 0
original_number = number  

while number != 0:
    digit = number % 10  
    reverse = reverse * 10 + digit 
    number = number // 10  

print("The reverse of " + str(original_number)+ " is " +str(reverse) + ".")