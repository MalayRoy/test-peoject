# Tuple
tuple=(1,2,3,2,1,5,6,6,4,5)
cnt_dict = {}

for num in tuple:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num]=1

print(cnt_dict)
        


