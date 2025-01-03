#!/usr/bin/env python3
import re

with open('input.txt.mini') as f:
    data = f.read()

def solve():
    register_p = r"[ABC]: (\d+)"
    program_p =  r"Program:\s([\d,]+)"
    A, B, C = list(map(int, re.findall(register_p, data)))
    instructions = list(map(int, re.findall(program_p, data, re.MULTILINE)[0].split(',')))
    #print(instructions)

    def operand_value(operand):
        if operand in [0, 1, 2, 3]:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        elif operand == 7:
            pass

    out = []
    idx = 0
    while idx < len(instructions):
        opcode = instructions[idx]
        operand = instructions[idx + 1]

        if opcode == 0:
            denominator = 2 ** operand_value(operand)
            A = A // denominator
        elif opcode == 1:
            B = B ^ operand
        elif opcode == 2:
            combo = operand_value(operand)
            B = combo % 8
        elif opcode == 3:
            if A != 0:
                idx = operand
                continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            combo = operand_value(operand)
            v = combo % 8
            out.append(v)
        elif opcode == 6:
            denominator = 2 ** operand_value(operand)
            B = B // denominator
        elif opcode == 7:
            C = A // 2 ** operand_value(operand)

        idx += 2
    return out

# part 1
print(','.join(map(str, solve())))