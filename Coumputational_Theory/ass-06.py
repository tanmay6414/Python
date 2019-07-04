"""
FINDING 2'S COMPLIMENT OF ANY BINARY NUMBER
Author  = Tanmay Pramod Varade
Date    = 26-09-2018
"""
a = raw_input("Enter your binary number : ")
r = ''

#take 2 empty lists
reverse_list = [] 
final_list = []

for i in range(len(a)):
	if a[i] == '1':
		reverse_list.append(0)
	elif a[i] == '0':
		reverse_list.append(1)


for i in range(len(a)):
	final_list.append(0)
final_list[len(a)-1] = 1


a1 =[]
a2 = []
a3 = []

for i in reversed(reverse_list):
	a1.append(i)
for i in reversed(final_list):
	a2.append(i)
print "a1 ",a1
print "a2 ",a2

for i in range(len(a1)):
	if a1[i] == a2[i] == 1:
		a3.append(0)
		a2[i+1] = 1
		
	elif a1[i] != a2[i]:
		a3.append(a1[i]+a2[i])
	if a1[i] == a2[i] == 0:
		a3.append(a2[i])

for i in reversed(a3):
	r+=str(i)
print r






print "Given string is : ", a
print "2's compliment is : ",r
