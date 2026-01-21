tuple1 = ((1, 2), (3, 4), (1, 7)) 

print(min(tuple1))
print(max(tuple1))        #Python compares tuples lexicographically (just like dictionary words).
# print(sum(tuple1))        # it will provide error


# for sum we need loop for nested tuple
tuple1 = ((1, 2), (3, 4), (1, 7))
total = sum(x for t in tuple1 for x in t)
print(total)
