ui = input("Enter a number : ")
print("The data type is originally ",(type(ui)))

unconv = int(ui)
print("Now the data type is : ",(type(unconv)))
power = unconv ** 8
print(ui, "raised to the 8th power is : ",power)
