tuple1 = ((1, 2), (3, 4), (5, 6)) 

print(tuple1.index((3,4)))




# Find index of 3 inside nested tuples
for i, t in enumerate(tuple1):
    if 3 in t:
        print(f"Found 3 in tuple index {i}")
