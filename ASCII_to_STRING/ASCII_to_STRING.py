def ascitostring(b):
	if len(b)==0:
		print("Please enter valid string...")
	if len(b)==1:  
		s=int(b[0])
		a1.append(chr(s))
	if len(b)==2:
		s=int(b[0]+b[1])
		a1.append(chr(s))
	if len(b)>2:
		s=int(b[0]+b[1]+b[2])
		if s>122:
			s=int(b[0]+b[1])
			a1.append(chr(s))
			b=b[2:]
			ascitostring(b)
		else:
			a1.append(chr(s))
			b=b[3:]
			ascitostring(b)
			

a=input("Enter ASCII value : ")
b=list(a.strip())
a1=[]
ascitostring(b)
		
		
main1=""
for i in a1:
	main1+=i
print(main1)