list1 = [1, 2, 3, 4, 5]

print(list1)
print("append 4")
list1.append(4)
print(list1)            #4 is appended to the last in the list1

list1.append('akshay')
print(list1)

list1.append((1,2))     # list.append() takes exactly one argument
print(list1)


#practice 1
list2=[]
for i in list1:
    # print(i)
    list2.append(i)
    print(list2)

