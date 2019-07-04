"""
dictonary looks up string of character as a inpute
and return yes or no according to the word is present 
in a given set of return information about word
student need to create a file of word
"""
import linecache
from itertools import permutations



while 1:
	print ("\n1. Write a content in file\t2. Enter your string\t3. Quit")
	ch = input("Enter your choise : ")

	if ch == 1:
		a = raw_input("\nEnter your word : ")
		fp.write("\n%s"%a)

	elif ch ==2:
		s_list = []
		s_list1 =[]
		final_list = []
		s = ''

		file = 'ass4.txt'
		fp = open(file,'a+')
		print ("This is all content in the file :")
		for line in fp:
			print line
			count = len(open(file).readlines(  ))       #count no of line from file
		for i in range(count):
			a = linecache.getline(file,i+1)
			s_list.append(a)


		for words in s_list:
			for letters in words:
				if letters not in s_list1:
					s_list1.append(letters)


		s_list1 = map(lambda s: s.strip(), s_list1)    #for removing of '\n' symbol from list
		s_list1.remove('')							   #for removing of empty element  from list


		for list_words in s_list1:
			s += list_words
		print "\n"

		print "Final string after removing repitation : ",s


		str1 = raw_input("Enter string you want to find : ")
		final_list = []
		perms = [''.join(p) for p in permutations(s)]
		for i in perms:
			if str1 in i:
				final_list.append(i)
		print "List of possible word : \n\n\n",final_list
		print "Total Number of word Found = ",len(final_list)


	elif ch == 3:
		quit()



