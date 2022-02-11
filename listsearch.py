list=[]
n=int(input("enter the no. of elements: \n"))
i=0
flag=0
for i in range(0,n):
	c=int(input("enter the list elements"))
	list.append(c)
print(list)
key=int(input("enter the no.to be search \n"))
for i in range(0,n):
	if(list[i]==key):
		flag=flag+1
		break;
if(flag==0):
	print("element not found")
else:
	print("element found at",i+1)

