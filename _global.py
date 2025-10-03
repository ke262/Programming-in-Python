def sum(a, b):
    print("Hey I am summing ")
    c = a + b
    global z
    z = 0
    return c

z = 3
print(sum(3, 12))
print(z)