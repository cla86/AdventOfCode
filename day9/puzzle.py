#!/usr/bin/env python3
# https://adventofcode.com/2024/day/9

with open('input.txt.mini', 'r') as f:
    data = f.read().strip()

empty = None

disk = list()
for fi, f in enumerate(data):
    if int(f) != 0:
        if fi % 2 == 0:
            index = fi // 2
            for i in range(int(f)):
                disk.append(index)
        else:
            for i in range(int(f)):
                disk.append(empty)

# part 1
for segment in disk:
    if segment == empty:
        s_index = disk.index(segment)
        for rev_segment in disk[::-1]:
            if rev_segment != empty:
                r_index = len(disk) - 1 - disk[::-1].index(rev_segment)
                disk[s_index] = rev_segment
                disk.pop(r_index)
                break

print(sum([x * i for i, x in enumerate(disk) if x != None]))

# part 2
disk = list()
for fi, f in enumerate(data):
    
    if int(f) != 0:
        if fi % 2 == 0:
            index = fi // 2
            for i in range(int(f)):
                disk.append(index)
        else:
            for i in range(int(f)):
                disk.append(empty)

def defragment_list(lst):
    n = len(lst)

    def find_trailing_elements(start):
        last_value = None
        trailing_elements = []
        indexes = []

        for i in range(start, -1, -1):
            if lst[i] is None:
                continue
            if last_value is None:
                last_value = lst[i]
            if lst[i] == last_value:
                trailing_elements.append(lst[i])
                indexes.append(i)
            else:
                break
        return trailing_elements, len(trailing_elements), indexes


    def find_nones(length):
        count = 0
        start_index = -1

        for i in range(n):
            if lst[i] is None:
                if count == 0:
                    start_index = i
                count += 1
                if count == length:
                    return list(range(start_index, start_index + count))
            else:
                count = 0
        return None

    current_end = n - 1

    while current_end >= 0:
        trailing_elements, length, indexes = find_trailing_elements(current_end)
        current_end = min(indexes) -1
        nones = find_nones(length)

        if nones:
            if current_end < nones[0]:
                continue

            for i, idx in enumerate(nones):
                lst[idx] = trailing_elements[i]

            for i in indexes:
                lst[i] = '.'

    return lst

defragmented_list = defragment_list(disk)
print(sum([x * i for i, x in enumerate(disk) if x != None and x != '.']))