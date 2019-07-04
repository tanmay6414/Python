
#	DESICION MAKING FOR A LAWN TENNIS

server = opponent = 0
gamept = []
while 1:
	print"\n\n--------------------------------------\n1. Server \t 2. Opponent"
	entry = raw_input("Enter stage of game : " )

	if server >= 40 and opponent >=40:
		if entry == '1':
			server += 1
			if server == opponent+2:
				gamept.append([server,opponent])
				print server," : ",opponent
				print"--------------------------------------"
				print "\n\n\t\t\t**********************\n\t\t\tServer wins!!!!!!!!\n\t\t\t**********************"
				break
		
		elif entry == '2':
			opponent+=1
			if opponent == server+2:
				gamept.append([server,opponent])
				print server," : ",opponent
				print"--------------------------------------"
				print "\n\n\t\t\t**********************\nOpponent wins!!!!!!!!\n\t\t\t**********************"
				break
	elif entry == '1':		
		if server < 30:
			server += 15	
			opponent = opponent	
		elif server == 30:
			server += 10
			opponent = opponent		
		elif server == 40  :
			if entry == '1':
				print server," : ",opponent
				print "--------------------------------------"
				print "\n\n\t\t\t**********************\n\t\t\tServer wins!!!!!!!!\n\t\t\t**********************"
				gamept.append([server,opponent])
				break
	elif entry == '2':
		if opponent < 30:
			opponent += 15
			server = server
		elif opponent == 30:
			opponent += 10
			server = server
		if opponent > 40:
			if entry == '2':
				print server," : ",opponent
				print "--------------------------------------"
				print "\n\n\t\t\t**********************\nOpponent wins!!!!!!!!\n\t\t\t**********************"
				gamept.append([server,opponent])
				break
	gamept.append([server,opponent])
	print server," : ",opponent
	print"--------------------------------------"
print "\n\n++++++++++++++++++  SCORE TABLE ++++++++++++++++++\n"
for i in range(len(gamept)):
	print "|\tServer - ",gamept[i][0],"\t:\t","Opponent - ",gamept[i][1],"\t|"
print "\n++++++++++++++++++++++++++++++++++++++++++++++++++\n"


		

