from string import ascii_lowercase as alphabet
from string import ascii_uppercase as ALPHABET

emoji = '😵‍💫'

# Columnar Transposition

key = 'bicycle'
message = 'transpositionscramblesletterslikepuzzlepieces'
ciphertext = 'tscsszcataeilssobteposeruerirllzepnlepinimtke'

"""
0123456
bicycle
-------
transpo
sitions
cramble
sletter
slikepu
zzlepie
ces

0246153

tscsszcataeilssobteposeruerirllzepnlepinimtke
"""

"""
We know:
- key
- ciphertext
- lengths

We want to calculate:
- the "depth" of the grid: depth = len(ciphertext) // len(key)
- the "stop" of the last grid line: stop = len(ciphertext) % len(key)
- if the original index of the column is < stop
- generate order of original columns from key (generate_columnar_key)
- pull out columns from ciphertext slice from "start" for "length"
- pad (i.e. add space) and zip columns
- plaintext message

Method
- rebuild the grid

column 0: start  0, up to  7 (column < stop)
column 2: start  7, up to 14 (column < stop)
column 4: start 14, up to 20
column 6: start 20, up to 26
column 1: start 26, up to 33 (column < stop)
column 5: start 33, up to 39
column 3: start 39, up to 45

0246153
-------

"""