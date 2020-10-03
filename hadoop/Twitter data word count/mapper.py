#!/usr/bin/python3

import sys
text=[]
date=[]
for line in sys.stdin:
     text.append(line.split(',')[0])
     date.append(line.split(',')[1])
for i in range(1,len(date)):
     date[i]=date[i].split(' ')[0]
for j in range(1,len(text)):
   for i in text[j].split(' '):
      if(len(i)==0): continue
      else:
        print(i+' '+date[j],',',1)
