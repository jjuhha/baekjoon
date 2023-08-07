from itertools import combinations
import sys

selection, option = map(int, sys.stdin.readline().split())
input_list = list(sys.stdin.readline().split())
input_list = sorted(input_list)
vowels =  'aeiou' #['a','e','i','o','u']
consonants = 'bcdfghjklnmpqrstvwxyz'

#
# for _ in range(option)

for i in combinations(input_list,selection) :
    i = ''.join(i)
    count_vowels = 0
    count_consonants = 0
    for j in i :
        if j in vowels :
            count_vowels += 1
        if j in consonants :
            count_consonants += 1
    if count_vowels >= 1 and count_consonants >= 2 :
        print(i)