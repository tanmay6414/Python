from qrtools import QR
User_history_file=open("User_history.txt","a+")

class TC(object):
	"""docstring for TC"""
	def extract(self):
		pnr=raw_input("Enter PNR no.:\t")
		# Python 2.x program to Scan and Read a QR code
		my_QR = QR(filename = pnr+".png")
		 
		# decodes the QR code and returns True if successful
		my_QR.decode()
		 
		# prints the data
		print my_QR.data

	def validate(self):
		pnr=raw_input("Enter PNR no:\t")
		
		for l in User_history_file.readlines():
			pnr_database,info=l.split("-",1)			

			if pnr==pnr_database:
				print l

if __name__ == '__main__':	
	while True:
		print "\n1.form Image\t 2.From PNR No 3.Back"
		choice=raw_input("Enter your choice:\t")

		if choice=='1':
			TC().extract()
		elif choice=='2':
			TC().validate()
		elif choice=='3':
			break
		else:
			print "Invalid choice!!!!"