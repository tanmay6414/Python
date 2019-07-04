#MONOAPBHABATICAL ALGORITHM FOR ENCRYPTION AND DECRY

lwr = 'abcdefghijklmnopqrstuvwxyz'
upr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lowr = []
uppr = []
#This two list is for assigning the  cipher or alter value of plane text
cipl = []
cipu = []
cipher = ''
plane = ''

#This is for to append value of two alphabatic string into list
for i in range(len(lwr)):
	lowr.append(lwr[i])       #appending k liye
	uppr.append(upr[i])
#This is for to append cipher text for the two apbhabatical string in reverse manner
cipl.append(lowr[::-1])
cipu.append(uppr[::-1])

while 1:
	print"\n\nWhat you want to do \n 1. Encrypt \t 2.Desrypt \t 3. Quit"
	ch = input("Enter your choice = ")

	if ch == 1:
		string = raw_input("Enter your string : ")
		for i in range(len(string)):
			for j in range(len(lowr)):
				if string[i] == lowr[j]: 	#This assign value of alpbhabate in string to the list of small letter list
					cipher += cipl[0][j] 	#This is for assigning plane text to the cipher text

				elif string[i] == uppr[j]:	#This assign value of alpbhabate in string to the list of small letter list
					cipher += cipu[0][j] 	#This is for assigning plane text to the cipher text

		print "\nYour cipher text is : ",cipher
		cipher = ''                             #This is because if we don't assign this value to empty string then every time in a while loop 'cipher' variable assign privious value

	elif ch == 2:
		string = raw_input("Enter your string : ")	
		# This is for desryption of massage just opposite to upper one
		for i in range(len(string)):
			for j in range(len(lowr)):
				if string[i] == cipl[0][j]:		
					plane = plane + lowr[j]

				elif string[i] == cipu[0][j]:
					plane = plane + uppr[j]
		print "\nYour plane text is : ",plane
		plane = ''								#This is because if we don't assign this value to empty string then every time in a while loop 'plane' variable assign privious value

	elif ch == 3:
		quit()

	else:
		print "Please insert correct choice"


"""
OUPPUT - 



C:\test\python\CSS>python Monoalphabatic.py


What you want to do
 1. Encrypt      2.Desrypt       3. Quit
Enter your choice = 1
Enter your string : tanmay

Your cipher text is :  gzmnzb


What you want to do
 1. Encrypt      2.Desrypt       3. Quit
Enter your choice = 2
Enter your string : gzmnzb

Your plane text is :  tanmay


What you want to do
 1. Encrypt      2.Desrypt       3. Quit
Enter your choice = 3

C:\test\python\CSS>
"""
