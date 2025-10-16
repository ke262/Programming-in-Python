def fibonacci(n):
    sequence = []
    a, b = 0, 1
    sequence.append(a)
    sequence.append(b)
    for i in range(2,n):
        a, b = b, a + b
        sequence.append(b)
    return sequence

print(fibonacci(100))   