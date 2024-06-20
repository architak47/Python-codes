def sum_all(*args):
    print(args) # (1, 2, 3, 4, 5)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3, 4, 5)) # 15