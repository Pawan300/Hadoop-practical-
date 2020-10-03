#!/usr/bin/python3
import sys
a=[]
for line in sys.stdin:
	a.append(line.strip())
N=int(a[-1][4])
for k in a:
	for i in range(1,N+1):
		if(k[0]=='A'):
			x=k.split(',')
			print(x[1],i,',',x[2],',',x[3])
		else:
			x=k.split(',')
			print(i,x[2],',',x[1],',',x[3])
