v=0
c=0
q=0
w=1
string=str(input("Enter the string \n"))
for i in string:
	if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" 
	or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
		v=v+1
	elif(i==" " or i=="  " or i=="   " or i=="    "):
		w=w+1
	elif(i=="?"):
		q=q+1
for i in string:
	if(i>="a" and i>="z"):
		c=c+1
	elif(i>="A" and i>="Z"):
		c=c+1
print("vowels:",v,"constants:",c,"question mark:",q,"words:",w)