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
    dict_1 = dict.fromkeys(list(s1), 0)
    dict_2 = dict.fromkeys(list(s2), 0)
    for ch in s1:
        dict_1[ch] += 1
    for ch in s2:
        dict_2[ch] += 1
    print(dict_1 == dict_2)

# is_anagram('abc', 'cbaa')


def count_hi(str):
    i = 0
    count = 0
    while i < len(str):
        temp_i = 0
        try:
            temp_i = str.index("hi", i)
        except:
            return count
        else:
            count += 1
        i = temp_i + 2
    return count

#print(count_hi('   hihi_hi+-hi'))


def cat_dog(str):
    cats_count = 0
    dogs_count = 0
    for i in range(len(str)-2):
        if str[i:i+3] == 'cat':
            cats_count += 1
        elif str[i:i+3] == 'dog':
            dogs_count += 1
    return dogs_count == cats_count
