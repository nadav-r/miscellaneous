"""
Identifiers:

\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
.  any character except for a newline
\b the whitespace around word
\. a period 

Modifiers:

{1,3} we're excepting 1-3
+ Macth 1 or more 
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ matching the beginning of a string
| either or  
[] range or "variance" [A-Za-z]  [1-5a-qA-Z] (any of these)
{5} 
{x} expecting "x" amount

White space characters: 

\n new line
\s space
\t tab
-------
\e escape
\f form feed
\r return 


DONT FORGET! :
. +  * ? [] $  ( ) { } | \

"""

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)


ageDict = {}
x=0

for eachName in names:
    ageDict[eachName] = ages[x]
    x +=1 

print(ageDict)
