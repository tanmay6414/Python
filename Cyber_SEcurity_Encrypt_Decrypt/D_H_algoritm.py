"""

#append value of alphabate in list
aa = {}
string1 = 'abcdefghijklmnopqrstuvwxyz'
string11 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(string1)):
	aa.update({string1[i]:i+1})
	aa.update({string11[i]:i+1})



# number is prime or not
a = input("Enter a number: ")
condition = 'ab'
for i in range(2,a-1):
	if a % i == 0:
		condition = 'z'
		print a, " is not a prime number"
		break
	elif a % i != 0:
		pass
if condition == 'ab':
	print a, " is a prime number"

"""
