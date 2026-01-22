a = [1,3,4,6,7]
b = [2,5,8,9,10]
c = int(input("Enter a number between 1 to 10:"))

if c in a:
    print("you have picked number from list a")
elif c in b:
    print("you have piced number from list b")
else:
    print(f"enter number between 1 to 10 you entered wrong number {c}:")