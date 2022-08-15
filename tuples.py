# Tuple are immutable
tuple1 = 1, 2, 3, 4
tuple2 = ("this", 'is', 'a', 'tuple', 'too')

a = tuple2.count("this")
b = tuple1.count(2)
print(a, b)
print(tuple1.index(4))