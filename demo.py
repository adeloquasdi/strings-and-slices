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

Method
- rebuild the grid

We want to calculate:
- the "depth" of the grid: depth = len(ciphertext) // len(key)
- the "stop" of the last grid line: stop = len(ciphertext) % len(key)
- if the original index of the column is < stop (in order to know that column's depth)
- generate order of original columns from key (generate_columnar_key)
- pull out columns from ciphertext slice from "start" for "length"
- pad (i.e. add space) and zip columns
- plaintext message

column 0: start  0, up to  7 (column < stop)
column 2: start  7, up to 14 (column < stop)
column 4: start 14, up to 20
column 6: start 20, up to 26
column 1: start 26, up to 33 (column < stop)
column 5: start 33, up to 39
column 3: start 39, up to 45

  0123456789
0 tscsszcata
1 eilssobtep
2 oseruerirl
3 lzepnlepin
4 imtke

0123456
-------
transpo
sitions
cramble
sletter
slikepu
zzlepie
ces    

transpositionscramblesletterslikepuzzlepieces
"""

def decrypt_columnar_transposition(ciphertext: str, key: str) -> str:
    # the "depth" of the grid
    depth = len(ciphertext) // len(key)
    # the "stop" of the last grid line:
    stop = len(ciphertext) % len(key)
    # generate order of original columns from key (generate_columnar_key)
    indices = []
    for index, _ in sorted(enumerate(key), key=lambda t: t[1]):
        indices.append(index)
    # pull out columns from ciphertext slice from "start" for "length"
    grid = [None] * len(key)
    start = 0
    for index in indices:
        # if the original index of the column is < stop
        if index < stop:
            column_depth = depth + 1
            grid[index] = ciphertext[start:start + column_depth]
            start += column_depth
        else:
            column_depth = depth
            # pad (i.e. add space)
            grid[index] = ciphertext[start:start + column_depth] + ' '
            start += column_depth
    plaintext = ''
    # zip columns
    for row in zip(*grid):
        plaintext += ''.join(row)
    # plaintext message
    return plaintext.rstrip('')




