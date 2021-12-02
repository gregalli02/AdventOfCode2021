# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:08:30 2021
@author: fracuci
"""

fh = open('numberDay2.txt','r')

lines = fh.readlines()

### second part - check submarine's user manual and use aim!!!

h_pos = 0
d_pos = 0
aim = 0

for i in range(0, len(lines)):
    instruction = lines[i].split(sep=' ')
    #print('command:', instruction[0], 'lenth:', instruction[1])
    if instruction[0] == 'forward':
        h_pos += int(instruction[1])
        d_pos += aim*int(instruction[1])
    if instruction[0] == 'down':
        aim += int(instruction[1])
    if instruction[0] == 'up':
        aim -= int(instruction[1]) 
        
print('horizontal_new:', h_pos, 'depth_new:', d_pos)
print('horizontal x depth NEW:', h_pos*d_pos)

fh.close()
