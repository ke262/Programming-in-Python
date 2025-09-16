def add(a, b):
    x = a + b
    return x


c = add(3, 5)
print(c)



def add(a, b, plus=0):
    x = a + b + plus
    return x


c = add(3, 5, 2)
print(c)



