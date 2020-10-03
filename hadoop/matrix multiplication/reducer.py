#!/usr/bin/python3
import sys
i=0
sum1=0
for line in sys.stdin:
	if(i==0):
		x=line.strip().split(',')
		i=1
	if(i==1):
		y=line.strip().split(',')
		print(y[0])
		print(x[0])
		if(y[0]==x[0]):
			if(x[1]==y[1]):
				sum1+=int(x[2])*int(y[2])
			x=y
			continue
			print(x[0],sum1)
			sum1=0
		
			
