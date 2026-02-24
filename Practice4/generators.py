# 1️ Generator that generates squares up to N
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2


# 2️ Generator for even numbers from 0 to n
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


# 3️ Generator for numbers divisible by 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


# 4️ Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


# 5️ Generator countdown from n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# TESTING PART

if __name__ == "__main__":

    print("1) Squares up to N:")
    n = int(input("Enter N: "))
    for value in square_generator(n):
        print(value)

    print("\n2) Even numbers from 0 to N (comma separated):")
    n = int(input("Enter N: "))
    print(",".join(str(num) for num in even_numbers(n)))

    print("\n3) Numbers divisible by 3 and 4:")
    n = int(input("Enter N: "))
    for num in divisible_by_3_and_4(n):
        print(num)

    print("\n4) Squares from a to b:")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    for value in squares(a, b):
        print(value)

    print("\n5) Countdown from N to 0:")
    n = int(input("Enter N: "))
    for num in countdown(n):
        print(num)