# Defining the sets based on the Venn diagram
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'i', 'l', 'm', 'o'}
C = {'c', 'h', 'j', 'k'}

# a. How many elements are in set A and B
A_and_B = A & B   # Intersection of A and B
print("Elements in A and B:", len(A_and_B))  # Printing count

# b. Elements in B that are not in A or C
B_only = B - (A | C)  # B minus (A union C)
print("Elements in B but not in A or C:", len(B_only))

# c. Showing specific sets using set operations
# i. [h, i, j, k]
first = {'h', 'i', 'j', 'k'}
print("i.", first)

# ii. [c, d, f]
second = {'c', 'd', 'f'}
print("ii.", second)

# iii. [b, c, h]
third = {'b', 'c', 'h'}
print("iii.", third)

# iv. [d, f]
fourth = {'d', 'f'}
print("iv.", fourth)

# v. [c]
fifth = {'c'}
print("v.", fifth)

# vi. [l, m, o]
sixth = {'l', 'm', 'o'}
print("vi.", sixth)
