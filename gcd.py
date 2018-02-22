print("\n")
m = int(input("Enter 1st number : "))
fm = []
for i in range(1,m+1):
	if(m%i==0):
		fm.append(i)
print(fm)

print("\n")

n = int(input("Enter 2nd number : "))
fn = []
for j in range(1,n+1):
	if(n%j==0):
		fn.append(j)
print(fn)

print("\n")

cf=[]
for f in fm:
	if f in fn:
		cf.append(f)

print("Common factors are : ",cf)
print("\n")
print("The GCD is : ",cf[-1])
