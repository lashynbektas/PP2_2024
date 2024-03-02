# Implement a generator that returns all numbers from (n) down to 0.

def reduce(n):
    for i in range(0, n):
        yield n - i
print(*reduce(10), sep=", ")