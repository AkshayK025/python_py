myset = set()   #empty set
print(myset,type(myset))

num = {1,3,4,5,8,10}

# You can add elements to a set using the add() method. However, if you try to add a duplicate element, it will not be added.
print(num)
num.add(222)    
print("222 is added in set:",num)