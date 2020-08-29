#!/usr/bin/env python

import sys

for line in sys.stdin:
  line = line.strip()
  key_value = line.split(",")
  key = key_value[0].split(" ")
  if len(key) >=2:
     date, word = key[0], key[1]
     value = key_value[1]
     
     print("{0}\t{1}".format(word, date+" "+value))
  else:
     print("{0}\t{1}".format(key_value[0], key_value[1]))

