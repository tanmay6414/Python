import socket                    #this is for importing socket connection            
while 1:
	n = input("\nEnter first prime number (n): ") 
	g = input("Enter second prime number (g): ")    #n and g accept prime number values
	
	def isprime(q):				#this function is for checking value of n and g are prime or not
	    for i in range(2,int(q**0.5)+1):
	        if q%i==0:
	            return False
	    return True

	if isprime(n) and isprime(g):      #if value is prime then proceed
		x = input("\nEnter any number(x) : ")
		a = (pow(g,x)) % n 
		print "\nOpen client side code........"

		s = socket.socket()   #assignning socket       
		port = 12345

		s.bind(('localhost', 12345))  #for binding socket to localhost or any other ip address      
		s.listen(5)   #this is for listening the value  		
		c, addr = s.accept()     

		nval = "\nValue of n = " + str(n)
		gval = "\nValue of g = " + str(g) 
		aval = "\nValue of a = " + str(a)


		
		c.send(nval)
		c.send(gval)
		c.send(aval)   #c.send() send this value to client side

		c.close()    #for closing socket
		
		b = input("Enter value of b : ")
		k1 = (pow(b,x)) % n      #calculate value of k1
		print "\nValue of k1: ",k1
		break
	#if numberis not prime then proceed this
	else:
		print 'Please enter prime number....'

"""
OUTPUT-


C:\test\python\CSS>python Diffie-Hellman_Server.py

Enter first prime number (n): 13
Enter second prime number (g): 17

Enter any number(x) : 2

Open client side code........
Enter value of b : 9

Value of k1:  3
"""



