val1 = input("Enter a String Element : ")
val2 = int(input("Enter a Integer Element : "))
val3 = float(input("Enter a Float Element : "))

print("\n")

lst = [val1,val2,val3]
tup = (val1,val2,val3)
dit = {"First Element":val1, "Second Element":val2, "Third Element":val3}

print("List of all Elements is : ",lst)
print("Tuples of all Elements is : ",tup)
print("dictionary of all Elements is : ",dit)

print("\n")

lst.append("More")
print("Updated list is : ",lst)

