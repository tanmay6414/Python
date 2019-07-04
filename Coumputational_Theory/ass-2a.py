# EQUAL NO'S OF A FOLLOWED BY EQUAL NO'S OF B
#TAnmay Pramod VArade
loop = False
tanmay = raw_input("\n\n\nEnter your string : ")
if len(tanmay) % 2 == 0:
	for i in range(0,len(tanmay)/2):
		for j in range(len(tanmay)/2,len(tanmay)):
			if tanmay[i] == 'a' and tanmay[j] == 'b' and tanmay[0] == 'a':
				loop = True
				pass
			else:
				print "Given string is NOT satisfy DFA condition."
				quit()
else:
	print "Given string is NOT satisfy DFA condition."
	quit()
if loop == True:
	print "Given string satisfy DFA condition."
if tanmay == '':
	print "Given string satisfy DFA condition."
