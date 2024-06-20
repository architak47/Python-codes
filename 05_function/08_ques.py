def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="archit", power="coding")
print_kwargs(name="awasthi")
print_kwargs(name="archit", power="coding", age=20)