import sys
from itertools import zip_longest
"""Find all permutations of a string"""


def permutation_list(s, pemutation=''):
    all_permutations = []
    if s == '':
        return [pemutation]
    for i, ch in enumerate(s):
        all_permutations += permutation_list(s[:i] + s[i+1:], ch + pemutation)
    return all_permutations

# print(sorted(permutation_list('bla')))


"""Reverse a string"""

# option 1


def my_reverse(s):
    return ''.join(list(reversed(s)))

# option 2


def my_reverse_2(s):
    s = list(s)
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return ''.join(s)

# option 3 recursive


def my_reverse_3(s, reversed_s=''):
    if s == '':
        return ''
    return my_reverse_3(s[1:]) + s[0]


# print(my_reverse_3(sys.argv[1]))


''' check if s1 and s2 are anagrams '''


def is_anagram(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')
    s1 = s1.lower()
    s2 = s2.lower()
    dict_1 = dict.fromkeys(list(s1),0)
    dict_2 = dict.fromkeys(list(s2),0)
    for ch in s1:
        dict_1[ch]+=1
    for ch in s2:
        dict_2[ch]+=1
    print(dict_1==dict_2)
    
#is_anagram('abc', 'cbaa')


'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

'''

def increment_string(strng):
    