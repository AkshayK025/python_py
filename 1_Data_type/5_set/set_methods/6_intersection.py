num1 = {1,3,4,5,8,10}
num2= {1,3,5,8,222}
print(len(num1),len(num2))

#Returns the common elements from two sets.
print()
print(num1.intersection(num2),len(num1.intersection(num2)))

# also you can do it in another way
print()
num3 = num1 & num2
print(num3,len(num3))