#	NO'S OF A'S DIVISIBLE BY 2
#TAnmay Pramod VArade
tanmay = raw_input("\n\nEnter your string : ")
a = 0
count = 0
for i in range(len(tanmay)):
	if tanmay[i] == 'a' or tanmay[i] == 'b':
		if tanmay[i] == 'a':
			count += 1
		else:		
			pass	
	else:
		a=1 
		break
if a==1:
	print "Given string is NOT satisfy DFA condition.\n"
while a==0:
	if count % 2 == 0 and count != 0:
		print "Given string satisfy DFA condition.\n"
		break
	else:
		print "Given string is NOT satisfy DFA condition.\n"
		break

		

