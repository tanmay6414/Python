def tern_dec(num):
	n=int(num)
	l=len(str(num))
	digit=0
	tern=0
	for i in range(0,l):
		digit=n%10
		tern+=pow(3,i)*digit
		n=n//10
	print tern

tern_dec(202212)