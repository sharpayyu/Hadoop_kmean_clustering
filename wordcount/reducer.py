#!/usr/bin/env python  
"""reducer.py"""

import sys  

total_count = 0

for line in sys.stdin:
    line_number, count = map(int, line.strip().split('\t'))
    total_count += count

# Output the total count to STDOUT
print(total_count)
