numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_cnt = 0
for num in numbers:
    if num > 0:
        positive_cnt += 1
        
print("total positive numbers are", positive_cnt)