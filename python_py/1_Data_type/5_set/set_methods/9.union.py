num1 = {1,3,4,5,8,10}
num2= {1,3,5,8,222}
print(num1,num2,sep='\n')
print(len(num1),len(num2))

# Combines all elements from two sets, removing duplicates.
print(num1.union(num2))
print(len(num1.union(num2)))