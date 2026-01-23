pairs = [(1, 2), (3, 1), (5, 0)]
pairs_sorted = sorted(pairs, key=lambda x: x[1])
print(pairs_sorted)  


print()
# This does exactly the same thing.
def get_second_item(x):
    return x[1]

pairs_sorted_def= sorted(pairs, key=lambda x: x[1])
print(pairs_sorted_def)

