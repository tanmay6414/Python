
#		VENDING MACHINE
sum = 0
while 1:
	print "\n\n\n--------------------------------------------------\n Which Coin you want to Insert..\n"
	print "1. 25 Rupees Coin \t\t 2. 100 Rupees Coin"
	coin = input("Enter Your Coin : ")

	if coin == 1:
		sum += 25
		if sum >= 125:
			print "\nYour Total Amount is = ",sum
			print "--------------------------------------------------"
			print "\n\n\n\n\t\t\t++++++++++++++++++++++++\n\t\t\t Take your Soda !!!\n\t\t\t Thanku for using me...\n\t\t\t++++++++++++++++++++++++"
			break
		elif sum < 125:
			print "\nYou have not enouh money. You only have ",sum,"Rupees"
			print "\nYour Total Amount is = ",sum
			print "-------------------------------------------------"


	elif coin == 2:
		sum += 100
		if sum >= 125:
			print "\nYour Total Amount is = ",sum
			print "-------------------------------------------------"
			print "\n\n\n\n\t\t\t++++++++++++++++++++++++\n\t\t\t Take your Soda !!!\n\t\t\t Thanku for using me...\n\t\t\t++++++++++++++++++++++++"
			break
		elif sum < 125:
			print "\nYou have not enouh money. You only have ",sum,"Rupees"
			print "\nYour Total Amount is = ",sum
			print "-------------------------------------------------"
	else:
		print"\n\t\t\tPlease enter correct coin !!!!"
		
	
