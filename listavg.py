list=[]
sum=0
n=int(input("enter the size of list \n"))
print("enter the elments of the list")
for i in range (0,n):
	c=int(input(""))
	list.append(c)
print("the average of numbers:")
for i in range (0,n):
	sum=sum+list[i]
avg=sum/n
print(avg)
print("The square of the each number:")
for i in range(0,n):
	sq=list[i]*list[i]
	print(sq)