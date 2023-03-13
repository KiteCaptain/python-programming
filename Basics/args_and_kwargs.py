# Allows an infinite number of arguments
def sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum(1.4,5,6,4,6,3,6,))


def total(**kwargs):
    tot = 0
    for k, v in kwargs.items():
        tot += v
    return round(tot, 2)

print(total(tea=12.453, coff=34.84736, buns=12.2421))