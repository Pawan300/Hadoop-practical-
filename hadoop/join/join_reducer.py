#!/usr/bin/env python

import sys 
previous_word = ""
line = 0

count_arr = []
date_count_arr = []

for line in sys.stdin:
  key , value = line.strip().split("\t")
  value = value.split()

  if line ==0:
    line = 1
    previous_word = key
    if len(value)>=2:
    	date_count_arr.append(value)
    else: count_arr.append(value)
  
  if previous_word == key:
     if len(value) >=2:
     	date_count_arr.append(value)
     else: count_arr.append(value)     
  
  if previous_word != key:
    for i in count_arr:
      for j in date_count_arr:
         print(previous_word, j[0],j[1], i[0])
    count_arr = []
    date_count_arr = []
    
    previous_word = key
    if len(value)>=2:
    	date_count_arr.append(value)
    else: count_arr.append(value)

for i in count_arr:
      for j in date_count_arr:
         print(key, j[0],j[1], i[0])
