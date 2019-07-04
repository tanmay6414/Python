#A'S DIVISIBLE BY 4 AND B'S ARE NOT DIVISIBLE BY 3

nOa = nOb = 0
tanmay = raw_input("\n\nEnter your String of  : ")
for i in range(len(tanmay)):
	if tanmay[i] == 'a':
		nOa += 1
	elif tanmay[i] == 'b':
		nOb += 1
	else:
		print "Please enter correct String !!!!!!!!!!!"
		quit()
if nOa % 4 == 0 and nOb % 3 !=0:
	print "Given string satisfy DFA condition."
else:
	print "Given string is NOT satisfy DFA condition."
