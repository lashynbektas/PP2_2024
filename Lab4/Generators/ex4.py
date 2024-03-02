# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2


print(*squares(10, 20))