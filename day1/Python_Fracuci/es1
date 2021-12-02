# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:41:26 2021
@author: fracuci
"""


fh = open('numberDay1.txt', 'r')

lines = fh.readlines()

### first part -  how many measurements are greater than the previous one?

first_count = 0

for i in range(0, len(lines)):    
    #print(lines[i])
    if i < len(lines)-1:
        measure_a = int(lines[i])
        measure_b = int(lines[i+1])
        
        if measure_b > measure_a:
            print(measure_b,'>',measure_a)
            first_count +=1 


print(first_count)


fh.close()
