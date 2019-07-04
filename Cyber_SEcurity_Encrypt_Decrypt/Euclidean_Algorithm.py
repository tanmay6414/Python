
#EUCLIDIAL KEY EXCHANGE 
#this is for taking input value from user
print "Please enter two coprime number"
r1 = input("Enter value of a :")
r2 = input("Enter value of b :")

q = r1 // r2  # for quotient
r = r1 % r2 #for remainder
nos = []
nos.append([q,r1,r2,r])  #this append into the list

while r != 0:#..............................This is for exchanging position of r1 and r2 and do this untill remainder is not zero
	r1 = r2 #for exchanging value of r1 to r2
	r2 = r  ##for exchanging value of r2 to r
	q = r1 // r2      # for quotient
	r = r1 % r2        #for remainder
	nos.append([q,r1,r2,r])   #again append


#This is for finding the value of x(gcd)
t1 = 1
t2 = 0
t = t1 - (nos[0][0]*t2)
tt = [] #...................................This list append value of t1, t2, t
tt.append([t1,t2,t])
for i in range(len(nos)-1):
	t1 = t2   #this is again exchanging value of t1 and t2
	t2 = t
	t = t1 - (nos[i+1][0]*t2)    #some ddefine formula			#
	tt.append([t1,t2,t])

x = tt[len(tt)-1][1]#........................This is because we have to find value of t up to the len(nos)

#if we not take this r1 and r2 value is final value from loop
r1 = nos[0][1]
r2 = nos[0][2]
y = ((nos[len(nos)-1][2])-(r1*x))/r2   #formulated part
print "\n+++++++++++++++++++++++++++++++++++++++++"
if nos[len(nos)-1][2] == 1:    #condition for coprime number
	print "Given two numbers are coprime numbers"
else:
	print "Given two numbers are not coprime numbers"
print "+\tgcd is        = ",nos[len(nos)-1][2],"\t\t+"
print "+\tPublic Key (y)    = ",y,"\t\t+"
print "+\tPrivate Key (x)   = ",x,"\t\t+"
print "+++++++++++++++++++++++++++++++++++++++++"



"""
OUTPUT -




C:\test\python\CSS>python Euclidean_Algorithm.py
Please enter two coprime number
Enter value of a :13
Enter value of b :18

+++++++++++++++++++++++++++++++++++++++++
Given two numbers are coprime numbers
+       gcd is        =  1              +
+       Public Key (y)    =  -5                 +
+       Private Key (x)   =  7          +
+++++++++++++++++++++++++++++++++++++++++

C:\test\python\CSS>python Euclidean_Algorithm.py
Please enter two coprime number
Enter value of a :888
Enter value of b :56

+++++++++++++++++++++++++++++++++++++++++
Given two numbers are not coprime numbers
+       gcd is        =  8              +
+       Public Key (y)    =  16                 +
+       Private Key (x)   =  -1                 +
+++++++++++++++++++++++++++++++++++++++++

C:\test\python\CSS>python Euclidean_Algorithm.py
Please enter two coprime number
Enter value of a :40
Enter value of b :69

+++++++++++++++++++++++++++++++++++++++++
Given two numbers are coprime numbers
+       gcd is        =  1              +
+       Public Key (y)    =  -11                +
+       Private Key (x)   =  19                 +
+++++++++++++++++++++++++++++++++++++++++

C:\test\python\CSS>python Euclidean_Algorithm.py
Please enter two coprime number
Enter value of a :789446
Enter value of b :2597412

+++++++++++++++++++++++++++++++++++++++++
Given two numbers are not coprime numbers
+       gcd is        =  2              +
+       Public Key (y)    =  -119478            +
+       Private Key (x)   =  393103             +
+++++++++++++++++++++++++++++++++++++++++

"""



