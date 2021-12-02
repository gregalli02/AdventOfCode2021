# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:08:30 2021
@author: CucinottaFr
"""

fh = open('numberDay2.txt','r')

lines = fh.readlines()

### first part - move the submarine

h_pos = 0
d_pos = 0

for i in range(0, len(lines)):
    instruction = lines[i].split(sep=' ')
    #print('command:', instruction[0], 'lenth:', instruction[1])
    if instruction[0] == 'forward':
        h_pos += int(instruction[1])
    if instruction[0] == 'down':
        d_pos += int(instruction[1])
    if instruction[0] == 'up':
        d_pos -= int(instruction[1]) 
    
print('horizontal:', h_pos, 'depth:', d_pos)
print('horizontal x depth:', h_pos*d_pos)

fh.close()
