#!/usr/bin/env python

import sys 

previous_word = ""
count_arr = 0
flag = False

for line in sys.stdin:
  key , value = line.strip().split("\t")
  
  if previous_word == key:
     if value.isalpha():
     	flag = True
     else: count_arr+=int(value)
  
  if previous_word != key:
    if flag:
         print(previous_word, count_arr)
    count_arr = 0
    flag = False
    
    previous_word = key
    if value.isalpha():
         flag =True
    else: count_arr+=int(value)

if flag:
         print(previous_word, count_arr)
