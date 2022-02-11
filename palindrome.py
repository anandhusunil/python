***********************************************************************
NAME: ANANDHU SUNIL
                             PALINDROME                      DATE:24-11-21
ROLL NO : 12
S3 IT
***********************************************************************
n=int(input("enter the number"))
temp=n
rev=0
while(temp>0):
	rem=temp%10
	rev=rev*10+rem
	temp=temp//10
if(n==rev):
	print(n,"is palindrome")
else:
	print(n,"is not palindrome")