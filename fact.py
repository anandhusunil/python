a=int(input("enter the number"))
fact=1
if(a==0):
	print("fact is 1")
else:
	for i in range (1,a+1):
		fact=fact*i
print("factorial is :",fact)