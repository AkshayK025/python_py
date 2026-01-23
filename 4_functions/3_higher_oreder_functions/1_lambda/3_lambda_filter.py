num = list(range(11))
print(num)

# map function
even_num = map(lambda x:x%2==0,num)
print(list(even_num))

print(),print("filter_lambda:")
even_num =filter(lambda x:x%2==0,num)
print(even_num),print(list(even_num))
