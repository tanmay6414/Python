while 1:

	p = input("Enter value of p : ")
	q = input("Enter value of q : ")
	def isprime(m):				#this function is for checking value of n and g are prime or not
	    for i in range(2,int(m**0.5)+1):
	        if m % i == 0:
	            return False
	    return True

	if isprime(p):
		if isprime(q):
			n = p*q
			print "n = ",n
			fiN = (p-1)*(q-1)
			print "fiN = ",fiN
			e = input("Enter value of e : ")
			coprime = []
			q = n // e
			r = n % e
			coprime.append([q,fiN,e,r])

			while r!=0:
				fiN = e
				e = r
				q = n // e
				r = n % e
				coprime.append([q,fiN,e,r])
			print coprime[len(coprime)-1][2]

			if coprime[len(coprime)-1][2] == 1 and e % n != 0 and e < fiN:
				e = coprime[0][2]
				k = input("Enter value of k : ")
				d = ((k*fiN)+1)/e
				print "d = ",d
				cipher = pow(81,e) % n
				plane = pow(cipher,d) % n
				print cipher
				print plane
			else:
				print "n"




