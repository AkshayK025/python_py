num1 = {1,3,4,5,8,10}
num2= {1,3,5,8,222}

# Checks if all elements of a set are contained in another set (subset).
print(num1.issubset(num2))

#elements are same but some are missing
num1 = {1,3,4,5,8,10}
num2 = {1,3,5,8}
print(num1.issubset(num2))

# all elements need to be same
num1 = {1,3,4,5,8,10}
num2 = {1,3,5,8,4,10}
print(num1.issubset(num2))
