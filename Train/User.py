import pyqrcode
import time
from random import *

localtime=time.localtime()
Time=time.asctime(localtime)

User_sigin_file=open("User_sigin.txt","a+")
route_file=open("route_database.txt","r+")
User_history_file=open("User_history.txt","a+")

class user(object):
	key=""	
	"""docstring for user"""

	def signup(self):
		name=raw_input("Name:\t")
		surname=raw_input("Surname:\t")
		address=raw_input("Address:\t")
		phone_no=raw_input("Phone no:\t")
		email=raw_input("E-mail id:\t")
		username=raw_input("Username:\t")
		passwd=raw_input("Password:\t")
		re_passwd=raw_input("Re-enter password:\t")


		while passwd!=re_passwd:
			print "Password doesn't match!!!\n"
			re_passwd=raw_input("Re-enter password:\t")
	
		if username=="" or passwd=="":
			print"Please enter username and password......"

		else:
			if username in dictionary:
				print "Username already exists.....Try another username"
			
			else:
				User_sigin_file.write(str(username+"	"+passwd+"	"+name+" "+surname+" "+address+" "+phone_no+" "+email)+"\n")
				print "Registration successfully...."


	def login(self):	
		f=False
		user.key=username=raw_input("Username:\t")
		password=raw_input("Password:\t")
		
		if username in dictionary:
			if dictionary[username]==password:
				print "Log in successfully...."
				return True			
		
		# print usernm,passwd
		print dictionary

		if f==False:
			print "Invalid username and password...."

		return f
	def buy_ticket(self):
		route_file.seek(0)	
		total_money=0;

		f=False
		for l in route_file.readlines():	
			print l.split("\n")
		
		people=input("Number of tickets booked:\t")
		
		source=raw_input("From:\t")
		destination=raw_input("To:\t")
		time=raw_input("Departure time:\t")

		try:
			hh,mm,ss=time.split(":")
		except Exception, e:
			print "Invalid time format..."
		else:

			if source==destination:
				print "source and destination never same!!!!!!"

			else:
				route_file.seek(0)
				for l in route_file.readlines():
					src,dst,t,price=l.split("-",3)
					print src,dst,t
					cost=int(price)
					print cost,people
					cost*=people
				
					if src.strip()==source and dst.strip()==destination and t.strip()==time:
						f=True
					
						confirm=raw_input("Enter your password to confirm ticket(press enter to cancle:)\t")
						if confirm==dictionary[user.key]:
							if cost==input(str(cost)+"Enter amount to pay\t"):

								if user.key in detail:

									x= str(randint(1, 100)) 
									q=pyqrcode.create("PNR no:"+x+"\nSource:-\t"+source+"\nDestination:-\t"+destination\
										+str(Time)+"\tNumber of tickets booked:\t"+str(people)+"\n\nCustomer details:-\n"+detail[user.key]	)
									q.png(x+'.png',scale=2)
									q.show()
									User_history_file.write(x+"-"+str(people)+"-"+source+"-"+destination+"-"+str(Time)+"\n")
									print "Ticket confirmed"
									print "PNR no:\t"+x+"\nSource:\t"+source+"\tDesitnation:\t"+destination\
									+"\n\nCustomer details:\n"+detail[user.key]
									break
						else:
							print "password does not match!!!! or you cancled it"
						
				if f==False:
					print "Given rout is not present!!!!" 
					
dictionary={}
detail={}
		
User_sigin_file.seek(0)
for l in User_sigin_file.readlines():
	username,passwd,info=l.split("	",2)

	dictionary[username.strip()]=passwd.strip()
	detail[username.strip()]=info.strip()

if __name__ == '__main__':
	u=user()	
	print "Welcome User\n\n"
	while True:
		f=False
		print "1.Log in \t2.Sign in \t3.Back"
		choice=raw_input("Enter your choice:\t")
		info =""

		print "detail",detail
		print dictionary
				
				
		
		if choice=='1':
			f=u.login()
		elif choice=='2':
			u.signup()
			
		elif choice=='3':
			break

		else:
			print "Invalid choice!!!!\n\n"

		if f==True:
			while True:
				print "\n\n1.Buy ticket \t2.Exit"
				choice=raw_input("Enter your choice:\t")

				if choice=='1':
					u.buy_ticket()

				elif choice=='2':
					break

				else:
					print "Invalid choice!!!!!\n\n"
			pass