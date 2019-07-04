#BINARY NO'S DIVISIBLE BY 5
#TAnmay Pramod VArade
a = raw_input("\n\nEnter your binary number : ")
number = 0
b = 0
for i in range(len(a)):
	if a[i] == '0' or a[i] == '1' or a[i]=='2':
		if a[i] == '1':
			number = number + pow(3,len(a)-i-1)
			print number
		else:
			pass
	else:
		b = 1
		break
if b==1:
	print "Given string is NOT satisfy DFA condition.\n"
while b==0:
	if number % 5 == 0 :
		print "Given string satisfy DFA condition.\n"
		break
	else:
		print "Given string is NOT satisfy DFA condition.\n"
		break

		