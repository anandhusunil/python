a=int(input("enter the lower range \n"))
r=int(input("enter the upper range \n"))
print("The prime numbers are : \n ")
for num in range(a,r+1):
	if(num>1):
		for i in range(2,num):
			if(num%i==0):
				break
		else:
				print(num)