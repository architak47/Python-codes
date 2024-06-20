cnt = 0

while True:
    cnt += 1
    if cnt >= 100:
        break
    number = int(input("Enter value between 1 and 10: "))
    if 1 <= number <= 10:
        print("thanks")
        break
    else:
        print("Invalid number, try again")