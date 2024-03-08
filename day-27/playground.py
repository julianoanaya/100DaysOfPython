def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(32, 5, 4, 9, 10))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #
    # print(kwargs["add"])
    n *= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
