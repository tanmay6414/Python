#	STARTING AND ENDING OF STRING WITH A
#TAnmay Pramod VArade
tanmay = raw_input("Enter your string : ")
flag = False
for i in range(len(tanmay)):
	
	if tanmay[i] == 'a' or tanmay[i] == 'b':
		if tanmay[0] == 'a' and tanmay[len(tanmay)-1] == 'a':
			flag = True
		else:
			print "Given string is NOT satisfy DFA condition."
			flag = False
			break
	else:
		print "Given string is NOT satisfy DFA condition."
		flag = False
		break
if flag == True:
	print  "Given string is satisfy DFA condition."
