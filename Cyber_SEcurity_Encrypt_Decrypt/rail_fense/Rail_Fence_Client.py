import socket               
s = socket.socket()         
port = 12345               
s.connect(('127.0.0.1', port))
print s.recv(1024)
s.close()       


a=[]
b=[]
f=''
c = raw_input("Enter a message you want to descrypt : ")
d=len(c)+1
e=len(c)
if e%2==0:
	for i in range(0,len(c)/2):
		a.append(c[i])
	for i in range(len(c)/2,len(c)):
		b.append(c[i])
else:
	for i in range(0,(len(c)/2)+1):
		a.append(c[i])
	for i in range((len(c)/2)+1,len(c)):
		b.append(c[i])

result = [None]*(len(a)+len(b))
result[::2] = a

result[1::2] = b
for j in range(len(result)):
	f+=result[j]
print "Your Original message is ",f
