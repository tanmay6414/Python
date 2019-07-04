#FIRST COME FIRST SERVE WITH ARRIVAL TIME

from __future__ import division
a=[]
sum = sum1 = sum2 = sum3 =0
st = []
wt = []
tt = []
n = input("how many processes you want to test = ")
for i in range(n):
	pname = raw_input("\nEnter process name: ")
	atime = input("Enter arrival time : ")
	btime = input("Enter brust time: ")
	a.append([pname,atime,btime])

a.sort(key = lambda x: x[1])

for i in range(len(a)):
	sum = sum 
	st.append(sum)
	sum = sum + a[i][2]
	wt1 = st[i] - a[i][1]
	wt.append(wt1)
	sum1 = sum1 + wt1
	sum2 = sum2 + a[i][2]
	tt.append(sum2)
	sum3 = sum3 + sum2 

awt = sum1/n
att = sum3/n
print"\n=========================================================================================================================="
print "Process Name\tArrival Time\tExecution Time\tService Time\tWaiting Time\tTurn Around Time"
for i in range(n):
	print '   ',a[i][0],'   \t\t',a[i][1],'   \t\t',a[i][2],'   \t\t',st[i],'   \t\t',wt[i],'   \t\t',tt[i]
print"=========================================================================================================================="

print "\nAverage Waiting Time is = ",awt
print "Average Turn Around Time is = ",att






"""
OUTPUT-


C:\test\python\OS>python FCFC.py
how many processes you want to test = 3

Enter process name: p1
Enter arrival time : 0
Enter brust time: 3

Enter process name: p2
Enter arrival time : 1
Enter brust time: 2

Enter process name: p3
Enter arrival time : 2
Enter brust time: 3

==========================================================================================================================
Process Name    Arrival Time    Execution Time  Service Time    Waiting Time    Turn Around Time
    p1                  0               3               0               0               3
    p2                  1               2               3               2               5
    p3                  2               3               5               3               8
==========================================================================================================================

Average Waiting Time is =  1.66666666667
Average Turn Around Time is =  5.33333333333

C:\test\python\OS>python FCFC.py
how many processes you want to test = 5

Enter process name: p1
Enter arrival time : 0
Enter brust time: 8

Enter process name: p2
Enter arrival time : 1
Enter brust time: 1

Enter process name: p3
Enter arrival time : 2
Enter brust time: 3

Enter process name: p4
Enter arrival time : 3
Enter brust time: 2

Enter process name: p5
Enter arrival time : 4
Enter brust time: 6

==========================================================================================================================
Process Name    Arrival Time    Execution Time  Service Time    Waiting Time    Turn Around Time
    p1                  0               8               0               0               8
    p2                  1               1               8               7               9
    p3                  2               3               9               7               12
    p4                  3               2               12              9               14
    p5                  4               6               14              10              20
==========================================================================================================================

Average Waiting Time is =  6.6
Average Turn Around Time is =  12.6
"""