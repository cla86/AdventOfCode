#!/usr/bin/env python3
from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().strip()

empty = None

disk = list()
for fi, f in enumerate(data):
    #print(fi, f)
    if int(f) != 0:
        if fi % 2 == 0:
            index = fi // 2
            for i in range(int(f)):
                disk.append(index)
        else:
            for i in range(int(f)):
                disk.append(empty)

print(len(disk))
for segment in disk:
    if segment == empty:
        s_index = disk.index(segment)
        for rev_segment in disk[::-1]:
            if rev_segment != empty:
                r_index = len(disk) - 1 - disk[::-1].index(rev_segment)
                disk[s_index] = rev_segment
                disk.pop(r_index)
                break

print(sum([x[0] * i for i, x in enumerate(disk) if x != None]))
    

        

        
#    for b in reversed(disk):
#        print(b)