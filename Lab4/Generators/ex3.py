# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divisible_by3_and4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print(*divisible_by3_and4(30), sep=", ")