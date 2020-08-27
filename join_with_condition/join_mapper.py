#!/usr/bin/env python
import sys

for line in sys.stdin:
  line = line.strip()
  key_value = line.split(",")
  key = key_value[0].split(" ")
  if key_value[1] == "ABC" or not key_value[1].isalpha():
     print("{0}\t{1}".format(key_value[0], key_value[1]))

