num1 = {1,3,4,5,8,10}
num2= {1,3,5,8,222}

print(len(num1),len(num2))
print()

#Returns elements that are in the first set but not in the second.
print(num1.difference(num2),len(num1.difference(num2)))

#or in another way
num3 = num1-num2
print(num3,len(num3))