num1 = {1,3,4,5,8,10}
num2= {1,3,5,8,222}

#Checks if a set contains all elements of another set (superset).
print(num1.issuperset(num2))

num1 = {1,3,4,5,8,10,222}
num2= {1,3,5,8,222}
print(num1.issuperset(num2))