
numbers = [12, 43, 12, 44, 43, 87, 33,45,67,90, 100, 200]
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)
