
A=[]
B=[]
print("enter the rows and columns of matrix")
row= int(input("rows : "))
column= int(input("columns : "))
print("enter the 1st matrix")
for i in range(0,row):
	r=[]
	for j in range(0,column):
		a=int(input())
		r.append(a)
	A.append(r)
print(A)
print("enter the 2st matrix")
for i in range(0,row):
	r=[]
	for j in range(0,column):
		a=int(input())
		r.append(a)
	B.append(r)
print(B)
result=[]
for i in range (0,row):
	r=[]
	for j in range (0,column):
		z=A[i][j]+B[i][j]
		r.append(z)
	result.append(r)
print("the result : ")
print(result)


