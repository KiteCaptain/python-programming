set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

set1.add(10)
set2.add(20)
set1.remove(5)
set2.remove(6)

# .union()
union = set1 | set2

# .intersection()
intersect = set1 & set2

# .difference()
diff = set1 - set2

# .symentric_difference()
symmetric = set1 ^ set2

print(set1)