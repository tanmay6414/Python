import random
username = 'tanny'
password = 'piddiii'
count = 0
a = username[:2]
b = password[:2]
n=1



user = raw_input("Enter username : ")
passw = raw_input("Enter password : ")



if user == username:


    if passw == password:
    	c = a + b + str(random.randint(100, 1000))
    	print "otp is : ",c
    	otp = raw_input("Enter your otp : ")
    	if otp == c:
    		print "Succesfully Login !!!"
    	elif(otp!=c):
    		while otp !=c and count<3:
    			print"\nPlease enter correct otp!!!"
    			otp = raw_input("Enter your otp : ")

    			if otp == c:
    				print "\nSuccesfully login !!!"
    			elif(otp!=c and count<3):
    				count += 1
    	if(count>2):
    		print"\nEnvalid otp!!!"


    
    elif(passw != password):

    	while passw != password and count<3:
    			print"you have enter wrong username or password\n please try again"
    			user = raw_input("Enter username : ")
    			passw = raw_input("Enter your password : ")
    			if user == username:
    			
    				if passw == password:
    					c = a + b + str(random.randint(100, 1000))
    					print "\notp is : ",c
    					otp = raw_input("Enter your otp : ")
    					if otp == c:
    						print "\nSuccesfully Login !!!"
    					else:
    						while otp !=c and count<3:
    							print"\nPlease enter correct otp!!!"
    							otp = raw_input("Enter your otp : ")

    							if otp == c:
    								print "Succesfully login !!!"
    							else:
    								count+=1
    					if (count>2):
    						print("\nEnvalid otp!!!")
    				else:
    					count += 1
    			else:
    				print"\nEnter correct username or password!!!"

    if (count>2):
    	print("Please try after some time!!!!!!")
    			

    				
else:	
	print"\nEnter correct username or password!!!"