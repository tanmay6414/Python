#SIMPLE ENCRYPTION DESCRYPTION

a = ''
while 1:
	
	print"\n What you want to do \n 1. Encrypt \t 2.Desrypt \t 3. Quit"
	x = input("\nEnter your choice = ")
	if x ==1:
		shift = input("BY how much you want to shift : ")  #this is for sthifting value of aplbhabate to specific shift
		c = raw_input("Enter the text you want to Encrypt : ")
		for i in c:
			b = ord(i) #result is ascii value of a alpbhabate
			a = a + chr(b+shift)  #This is for assign given text to specific shift & return the text value
		print(a)
		a = ''     #This is because if we don't assign this value to empty string then every time in a while loop 'a' variable assign privious value

	elif x == 2:
		shift = input("BY how much you want to shift : ")
		d = raw_input("Enter the text you want to Descrypt : ")
		for i in d:
			b = ord(i)
			a = a + chr(b-shift)  	#This is for reverse the shifting & return the text value
		print(a)
		a = ''     #This is because if we don't assign this value to empty string then every time in a while loop 'a' variable assign privious value

	elif x == 3:
		quit()
	else:
		print "\n \nPlease insert correct choice"


"""
OUTPUT-


C:\test\python\CSS>python Caesar_Cipher.py

 What you want to do
 1. Encrypt      2.Desrypt       3. Quit

Enter your choice = 1
BY how much you want to shift : 4
Enter the text you want to Encrypt : tanmay
xerqe}

 What you want to do
 1. Encrypt      2.Desrypt       3. Quit

Enter your choice = 2
BY how much you want to shift : 4
Enter the text you want to Descrypt : xerqe}
tanmay

 What you want to do
 1. Encrypt      2.Desrypt       3. Quit

Enter your choice = 3

"""
	


