e=''
a=[]
b=[]
f=''
c = raw_input("Enter a message : ")
for i in range(0,len(c),2):
	a.append(c[i])
for i in range(1,len(c),2):
	b.append(c[i])	
d = a + b
for i in range(len(d)):
	e+=d[i]


import socket               
s = socket.socket()         
print "Socket successfully created"
port = 12345               
s.bind(('localhost', port))        
print "socket binded to %s" %(port)
s.listen(5)     
print "socket is listening"           

c, addr = s.accept()     
print 'Got connection from', addr
c.send(e)
c.close()
