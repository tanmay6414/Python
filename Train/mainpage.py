from Admin import *	
from User import *
from TC import *
while True:
	print "*"*80,"\n"
	print "1.Admin \t2.User \t\t3Ticket Checker \t4.Exit"
	choice=raw_input("Enter your work choice:\t")

	if choice=='1':
		a=Admin()

		while True:
			print "*"*80,"\n"

			print "1.Log in \t2.Sign in \t3.Back"
			choice=raw_input("Enter your choice:\t")

			f=False
			if choice=='1':
				print "_"*80,"\n"
				f=a.login()
				print "_"*80,"\n"

			elif choice=='2':
				print "_"*80,"\n"
				a.signin()
				print "_"*80,"\n"

			elif choice=='3':
				break

			else:
				print "_"*80,"\n\n"
				print "Invalid choice!!!!!!!\n\n"

				print "_"*80,"\n\n"
			if f==True:
				while True: 
					print "*"*80,"\n"
					print "1.Add location \t2.Add route \t3.Modify route \t4.Back"
					choice=raw_input("Enter your choice:\t:")

					if choice=='1':
						print "_"*80,"\n"
						a.location(raw_input("Enter the city:\t"))
						print "_"*80,"\n"
					elif choice=='2':
						print "_"*80,"\n"
						a.add_route()
						print "_"*80,"\n"

					elif choice=='3':
						print "_"*80,"\n"
						a.modify_route()
						print "_"*80,"\n"
					
					elif choice=='4':
						break

					else:
						print "_"*80,"\n"
						print "Invalid choice!!!!!!!"
						print "_"*80,"\n"

			

	elif choice=='2':
			
		u=user()	
		while True:
			f=False
			print "*"*80,"\n"
			print "1.Log in \t2.Sign in \t3.Back"
			choice=raw_input("Enter your choice:\t")
			
			if choice=='1':
				print "_"*80,"\n"
				f=u.login()
				print "_"*80,"\n"
			elif choice=='2':
				print "_"*80,"\n"
				u.signup()
				print "_"*80,"\n"
				
			elif choice=='3':
				break

			else:
				print "_"*80,"\n"
				print "Invalid choice!!!!\n\n"
				print "_"*80,"\n"

			if f==True:
				while True:
					print "\n\n1.Buy ticket \t2.Back"
					choice=raw_input("Enter your choice:\t")

					if choice=='1':
						print "_"*80,"\n"
						u.buy_ticket()
						print "_"*80,"\n"

					elif choice=='2':
						break

					else:
						print "_"*80,"\n"
						print "Invalid choice!!!!!\n\n"
						print "_"*80,"\n"

	elif choice=='3':
			
		while True:
			print "*"*80,"\n"
			print "\n1.form Image\t 2.From PNR No 3.Back"
			choice=raw_input("Enter your choice:\t")

			if choice=='1':
				print "_"*80,"\n"
				TC().extract()
				print "_"*80,"\n"
			elif choice=='2':
				print "_"*80,"\n"
				TC().validate()
				print "_"*80,"\n"
			elif choice=='3':
				break
			else:
				print "_"*80,"\n"
				print "Invalid choice!!!!"
				print "_"*80,"\n"

	elif choice=='4':
		break
	else:
		print "_"*80,"\n"
		print "Invalid choice!!!!!!"
		print "_"*80,"\n"