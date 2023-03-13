from itertools import permutations, product, combinations, combinations_with_replacement

# Itertools .permutations()
my_string, n = "GERTRUDE", 8
my_string.split(' ')
for enum, i in enumerate(list(permutations(sorted(my_string), n))):
    # print(enum + 1, "".join(i))
    pass

# Itertools .product() for cartesian product
input_1 = "1 2"
input_2 = "3 4"
a = list(map(int,input_1.split(' ')))
b = list(map(int,input_2.split(' ')))

for i in product(a, b):
    # print(i)
    pass

# Itertools .combinations_with_replacement()
my_string, n = "EUGINE", 2
my_string.split(' ') 

for i in list(combinations_with_replacement(sorted(my_string), n)):
    # print(''.join(i))
    pass


# Itertools .combinations()
my_string, n = "NYAKUNDI", 4
for i in combinations(sorted(my_string), n):
    print(''.join(i))
