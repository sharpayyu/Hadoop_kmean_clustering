#!/usr/bin/env python  
"""mapper.py"""  
import sys  
 

for i, line in enumerate(sys.stdin, start=1):
    # Emit line number as the key and count as 1 for each line
    print('%d\t%s' % (i, 1))

# this script reads input from the standard input stream 
# and maps each line to a key value pair
# key is the line number
# value is the count of 1 for each line

# enumerate returns a tuple containing the line number and the line itselg
# print is used to output the key value pair to the standard output stream
# %d and %s are placeholders for the line number and the count of 1
# the values are substituted in the placeholders using the $ operator