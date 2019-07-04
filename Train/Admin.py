"""Functions:

1. Insert the data about seat details of particular coach.

2. Search the seat in the coach.

3. Mark present or absent to seat.

4. Allocate new seat to vacant place.

Extra functionality student may add to the project which will fetch extra grades.

Student must have following things in their code:

1. Indentions, Comments and formatting wherever necessary which will increase the readability of code.

2. Checking of all possible inputs.

3. Reusability.

4. Mention the Data structure used.

5. User Friendly.

add location : adding city
add route: mumbai-pune , pyne-nashk X  siyrce-destination
manage route: pune-ahamadabad  

"""
import os
Admin_sigin_file=open("Admin_sigin.txt","a+")
class Admin():
	"""docstring for Admin"""

	def login(self):		
		f=False
		username=raw_input("Username:\t")
		password=raw_input("Password:\t")

		if username in dictionary:
			if dictionary[username]==password:
				
				print "Log in successfully...."
				f=True	

		if f==False:
			print "Invalid username and password...."

		return f

	def signin(self):		
		username=raw_input("Username:\t")
		passwd=raw_input("Password:\t")

		if username=="" or passwd=="":
			print"Please enter username and password......"

		else:
			if username in dictionary:
				print "Username already exists.....Try another username"
			
			else:
				Admin_sigin_file.write(str(username+"-"+passwd)+"\n")
				print "Registration successfully...."

	def location(self,city):
		location_file=open("location_database.txt","a+")
		flag=False
		location_file.seek(0)
		for l in location_file.readlines():			
			if city==l.strip():
				print "Location already present..."
				flag=True
				break
		
		if flag==False:
			location_file.write(city+"\n")
			print "location added...." 

		location_file.close()
	def add_route(self):
		route_file=open("route_database.txt","a+")
		location_file=open("location_database.txt","a+")
		
		f=False
		source=raw_input("From:\t")
		destination=raw_input("To:\t")
		time=raw_input("Set departure time hh:mm:ss:\t")
		price=raw_input("price for tour:\t")
		try:
			hr,mm,ss=time.split(":",2)
			print hr,mm,ss
			
		except Exception, e:
			print "Time format is not correct!\n"
		
		else:
			if source=="" and destination=="" and time=="":
				print "Source and destination Can not set empty!!!"

			elif source==destination:
				print "source and destination never same!!!!!!"

			else:
				line=location_file.readlines()

				location_file.seek(0)	
				for l in line:
					if source == l.split() or destination==l.strip():
						route_file.write(source+"-"+destination+"-"+time+"-"+price+"\n")
						print "Route added...."
						f=True
						break
			
				if f==False:
					print "location not present!!!!!" 
		finally:
			route_file.close
			pass

	def modify_route(self):
		route_file=open("route_database.txt","a+")
		temp=open("Temp.txt","w+")
	
		route_file.seek(0)

		for l in route_file.readlines():
			print l.split("\n")
			
		source=raw_input("Enter source which want to modify:\t")
		destination=raw_input("Enter destination which want to modify:\t")
		time=raw_input("Enter departure time of the train:\t")
		price=raw_input("Enter price:\t")
		try:
			hh,mm,ss=time.split(":",2)
		
		except Exception, e:
			print "Time is not in format!!!!!\n"
		else:
			route_file.seek(0)
			for l in route_file.readlines():
				if l.strip()==source+"-"+destination+"-"+time+"-"+price.strip():# and l.split()==destination and l.split()==time and l.split()==price:
					destination=raw_input("destination")
					temp.write(source+"-"+destination+"-"+time+"-"+price+"\n")
					print "Modified"
				
				else :
					temp.write(l)
		finally:
			route_file.close()
			temp.close()
			os.remove("route_database.txt")
			os.rename("Temp.txt","route_database.txt")

a=Admin()
dictionary={}

Admin_sigin_file.seek(0)
for l in Admin_sigin_file.readlines():
	username,passwd=l.split("-",1)		
	dictionary[username.strip()]=passwd.strip()

if __name__ == '__main__':

	while True:

		print "1.Log in \t2.Sign in \t3.Back"
		choice=raw_input("Enter your choice:\t")




		if choice=='1':
			f=a.login()
		elif choice=='2':
			a.signin()

		elif choice=='3':
			break

		else:
			print "Invalid choice!!!!!!!\n\n"

		if f==True:
			while True: 
				print "1.Add location \t2.Add route \t3.Modify route \t4.Exit"
				choice=raw_input("Enter your choice:\t:")

				if choice=='1':
					a.location(raw_input("Enter the city:\t"))
				
				elif choice=='2':
					a.add_route()

				elif choice=='3':
					a.modify_route()
					pass

				elif choice=='4':
					break

				else:
					print "Invalid choice!!!!!!!"

		
		