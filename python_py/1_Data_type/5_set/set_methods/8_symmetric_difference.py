num1 = {1,3,4,5,8,10}
num2= {1,3,5,8,222}
print(num1,num2,sep='\n')
print(len(num1),len(num2))

#symmetric difference
#Returns elements that are in either of the sets, but not in both.
print(num1.symmetric_difference(num2))
print(len(num1.symmetric_difference(num2)))
