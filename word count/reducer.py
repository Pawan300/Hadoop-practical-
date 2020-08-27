#!/usr/bin/env python

import sys

last_key      = None             
running_total = 0
for input_line in sys.stdin:
    this_key, int(value) = input_line.strip().split("\t", 1)  
    if last_key == this_key: running_total += value   

    else:
        if last_key:             
            print( "{0}\t{1}".format(last_key, running_total) )
        running_total = value   
        last_key = this_key

if last_key == this_key:
    print( "{0}\t{1}".format(last_key, running_total)) 
	
