#!/usr/bin/env python3

from collections import defaultdict


class Stones:
    def __init__(self, value):
        self.value = value

    def zero_to_hero(self):
        self.value += 1
        return self

    def the_year_we_all_say_fuck_it(self):
        self.value *= 2024
        return self

    def split_stone(self):
        def removeLeadingZeros(num):
            for i in range(len(num)):
                if num[i] != '0':
                    res = num[i::]
                    return res
            return "0"
            
        if len(str(self.value)) % 2 == 0:
            half = len(str(self.value)) // 2
            left, right = map(int, (str(self.value)[:half], 
                                    removeLeadingZeros(str(self.value)[-half:])))
            
            return (Stones(left), Stones(right))
        return self

    def __repr__(self):
        return str(self.value)

class Blinking:
    def __init__(self, numbers):
        self.numbers = []
        for num in numbers:
            if isinstance(num, tuple):
                self.numbers.extend(Stones(n) for n in num)
            else:
                self.numbers.append(Stones(num))

    def zero_to_hero_all(self):
        for num in self.numbers:
            if num.value == 0:
                num.zero_to_hero()
        return self

    def the_year_we_all_say_fuck_it(self):
        for num in self.numbers:
            num.the_year_we_all_say_fuck_it()
        return self

    def split_stones(self):
        new_numbers = []
        for num in self.numbers:
            split_result = num.split_stone()
            if isinstance(split_result, tuple):
                new_numbers.extend(split_result)
            else:
                new_numbers.append(split_result)
        self.numbers = new_numbers
        return self
    
    def blink(self):
        new_numbers = []
        for num in self.numbers:
            if num.value == 0:
                new_numbers.append(num.zero_to_hero())
            elif len(str(num.value)) % 2 == 0:
                split_result = num.split_stone()
                if isinstance(split_result, tuple):
                    new_numbers.extend(split_result)
                else:
                    new_numbers.append(split_result)
            else:
                new_numbers.append(num.the_year_we_all_say_fuck_it())
        self.numbers = new_numbers
        return self.numbers

    def __repr__(self):
        return f"Blinking({self.numbers})"
    
    def __iter__(self):
        for num in self.numbers:
            yield num

with open('input.txt', 'r') as f:
    stones = list(map(int, f.read().split(' ')))

# part 1
plist = Blinking(stones)
number_of_blinks=25
for i in range(number_of_blinks):
    plist.blink()
    # print(i, len(list(plist)))

print(len(list(plist)))