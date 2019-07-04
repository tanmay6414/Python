import socket    #this is for importing socket connection            

port = 12345
s = socket.socket()                      
s.connect(('127.0.0.1', 12345))   #for binding socket to localhost or any other ip address  
print s.recv(1000000)
print s.recv(1000000)
print s.recv(1000000)   #this is for receiving value of n g and a from server side

n = input("Enter value of n : ") 
g = input("Enter value of g : ")
a = input("Enter value of a : ")
y = input("Enter another number(y) : ")   #any value of user



b = (pow(g,y)) % n   #calculate b   
print"\nValue of b : ", b

s.close()    #closing socket

k2 = (pow(a,y)) % n   #calculate k2 by formula
print "Value of k2 : ",k2


"""
OUTPUT-


C:\test\python\CSS>python Diffie-Hellman_Client.py

Value of n = 13
Value of g = 17
Value of a = 3


Enter value of n : 13
Enter value of g : 17
Enter value of a : 3
Enter another number(y) : 4

Value of b :  9
Value of k2 :  3
"""