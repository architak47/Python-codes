# username = "archit"

# def func():
#     username = "arc"
#     print(username)
# print(username)
# func()

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()

def chacha(num):
    def actual(x):
        return x ** num
    return actual


f = chacha(2)
g = chacha(3)

print(f(3))
print(g(3))