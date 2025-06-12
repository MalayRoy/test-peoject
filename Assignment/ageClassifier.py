# Write a Python program that takes a person's age as input and
# prints out whether they are an infant (0-1), toddler (1-3), child (4-12), teenager
# (13-19), adult (20+).


age = int(input("Enter the person's age: "))

if age < 0:
    print("Age cannot be negative. Please enter a valid age.")
elif 0 <= age <= 1:
    print("The person is an Infant.")
elif 2 <= age <= 3:
    print("The person is a Toddler.")
elif 4 <= age <= 12:
    print("The person is a Child.")
elif 13 <= age <= 19:
    print("The person is a Teenager.")
else:
    print("The person is an Adult.")