from __future__ import division

#https://www.youtube.com/watch?v=dOqybyMAlIs&index=12&list=RDvWpD7vw5Dn4
#https://www.youtube.com/watch?v=mEMHF5W4zlY&index=13&list=RDvWpD7vw5Dn4

class Process:
	def __init__(self,pid,at,bt):
		self.pid = pid
		self.arrival = at
		self.brust = bt
chart = []
def SJF(plist, n):
	global chart
	queue = []
	time = 0
	ap = 0
	rp = 0
	done = 0

	while (done < n):
		for i in range(ap,n):
			if time >= plist[i].arrival:
				queue.append(plist[i])
				ap+=1
				rp+=1
		if rp<1:
			time+=1
			chart.append(0)
			continue 
		queue.sort(key=lambda x:(x.brust,x.arrival))

		if queue[0].brust>0:
			chart.append(queue[0].pid)
			time+=1
			queue[0].brust-=1
			if queue[0].brust<1:
				queue[0].brust=99999999
				done+=1
				rp -=1


print "\n\n======================================================================================"
print "\t\t\t\t!!!WARNING!!!\n  Kindly enter Process no in terms of NUMBER and not like p1, p2, etc,etc !!!"
print "======================================================================================\n\n\n"




plist=[]
plist1=[]

nn = input("Enter no of process : ")
print "\n"

for i in range(nn):
	no=input("Enter Process No \t       : ")
	at1=input("Enter Arrival time for process : ")
	bt1=input("Enter Brust time for process   : ")
	print "\n"
	plist1.append([no,at1,bt1])
	plist.append(Process(no,at1,bt1))
	#plist = sorted(plist, key=lambda x: (x[0],x[1], x[2]))
plist1.sort(key = lambda x: x[0])

print plist1

SJF(plist,len(plist))
print '**********Gantt chart************\n',(chart)
z = []
for i in range(len(plist)):
	z.append(0)

sum = sum1 = 0
ttt = []
wtt = []
for i in range(len(chart)):
	for j in range(nn):
		if chart[i] == j+1:
			z[j] = i+1 

for i in range(nn):
	m = z[i] - plist1[i][1]
	n = m - plist1[i][2] 
	ttt.append(m)
	wtt.append(n)
	sum += m
	sum1 += n


att = sum/nn
awt = sum1/nn

print"\n\t\t\t\t==================================\n\t\t\t\t\t+ SRTF TABLE +"
print"====================================================================================================="
print "Process No\tArrival Time\tExecution Time\tWaiting Time\tTurn Around Time"
for i in range(nn):
	print '   ',plist1[i][0],'   \t\t',plist1[i][1],'   \t\t',plist1[i][2],'\t\t',wtt[i],'   \t\t',ttt[i]
print"\n====================================================================================================="

print "\nAverage Waiting Time is = ",awt
print "Average Turn Around Time is = ",att



"""
OUTPUT - 


C:\Users\DELL\Desktop>python SRTF.py


======================================================================================
                                !!!WARNING!!!
  Kindly enter Process no in terms of NUMBER and not like p1, p2, etc,etc !!!
======================================================================================



Enter no of process : 4


Enter Process No               : 1
Enter Arrival time for process : 0
Enter Brust time for process   : 7


Enter Process No               : 2
Enter Arrival time for process : 2
Enter Brust time for process   : 4


Enter Process No               : 3
Enter Arrival time for process : 4
Enter Brust time for process   : 1


Enter Process No               : 4
Enter Arrival time for process : 5
Enter Brust time for process   : 4


[[1, 0, 7], [2, 2, 4], [3, 4, 1], [4, 5, 4]]
**********Gantt chart************
[1, 1, 2, 2, 3, 2, 2, 4, 4, 4, 4, 1, 1, 1, 1, 1]

                                ==================================
                                        + SRTF TABLE +
=====================================================================================================
Process No      Arrival Time    Execution Time  Waiting Time    Turn Around Time
    1                   0               7               9               16
    2                   2               4               1               5
    3                   4               1               0               1
    4                   5               4               2               6

=====================================================================================================

Average Waiting Time is =  3.0
Average Turn Around Time is =  7.0

C:\Users\DELL\Desktop>python SRTF.py


======================================================================================
                                !!!WARNING!!!
  Kindly enter Process no in terms of NUMBER and not like p1, p2, etc,etc !!!
======================================================================================



Enter no of process : 6


Enter Process No               : 1
Enter Arrival time for process : 0
Enter Brust time for process   : 8


Enter Process No               : 2
Enter Arrival time for process : 1
Enter Brust time for process   : 4


Enter Process No               : 3
Enter Arrival time for process : 2
Enter Brust time for process   : 2


Enter Process No               : 4
Enter Arrival time for process : 3
Enter Brust time for process   : 1


Enter Process No               : 5
Enter Arrival time for process : 4
Enter Brust time for process   : 3


Enter Process No               : 6
Enter Arrival time for process : 5
Enter Brust time for process   : 2


[[1, 0, 8], [2, 1, 4], [3, 2, 2], [4, 3, 1], [5, 4, 3], [6, 5, 2]]
**********Gantt chart************
[1, 2, 3, 3, 4, 6, 6, 2, 2, 2, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1]

                                ==================================
                                        + SRTF TABLE +
=====================================================================================================
Process No      Arrival Time    Execution Time  Waiting Time    Turn Around Time
    1                   0               8               12              20
    2                   1               4               5               9
    3                   2               2               0               2
    4                   3               1               1               2
    5                   4               3               6               9
    6                   5               2               0               2

=====================================================================================================

Average Waiting Time is =  4.0
Average Turn Around Time is =  7.33333333333
"""




