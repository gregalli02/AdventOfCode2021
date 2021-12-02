# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:41:26 2021
@author: fracuci
"""

fh = open('numberDay1.txt', 'r')

lines = fh.readlines()

#### second part how many sum of a three-measurement sliding window are
#### larger than the previous three-measurement sum?


second_count = 0

for i in range(2, len(lines)):
    if i < len(lines)-1:
        sliding_window_a = int(lines[i-2]) + int(lines[i-1]) + int(lines [i])
        sliding_window_b = int(lines[i-1]) + int(lines[i]) + int(lines[i+1])
        
        if sliding_window_b > sliding_window_a:
            print(sliding_window_b,'>',sliding_window_a)
            second_count +=1
    
print(second_count)

fh.close()
