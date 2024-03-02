# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def range(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


numbers = range(10)
print(*numbers, sep=", ")