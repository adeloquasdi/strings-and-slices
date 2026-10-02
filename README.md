# Slices

Slices are an extended way of accessing elements of a sequence by
indices. There are two ways to create a slice:

1.  Explicitly by creating a `slice` object and assigning it to a
    variable
2.  Using colons in the square brackets following a sequence.

Slices work very similar to the `range` function, in that there are
three values which determine the values to be used: the `start` index,
the `stop` index, and the `step`.

``` python
result = []
for index in range(start, stop, step):
    result.append(some_list[index])

# is equivalent to

result = some_list[start:stop:step]
```

Like `range`, not all of (`start`, `stop`, and `step`) are required.

- `some_list[1:]` is all but the first element of the list (or the list,
  starting with index 1)
- `some_list[:-1]` is all but the last element of the list (or the list,
  up to index -1)
- `some_list[::-1]` is the list, but reversed

# Encoding

Encoding is a process by which we \"translate\" data from one form to
another. Most commonly, we will apply this to translating various kinds
of data which are not inherently numerical into numbers. But you could
think of letters as encoding sounds as visual symbols, and data networks
require encoding numbers as patterns of rising and falling voltage.
Encoding non-numerical data as numbers will also be very important as
you learn to apply statistical models to non-numerical data in the
future.

In the context of this course, however, we will almost always be talking
about **character** encoding. Python defaults to using **UTF-8** to
encode character data. UTF-8 encodes characters by assigning a number to
each character. You can convert between these numbers and
single-character strings using the `chr(i: int) -> str` and
`ord(character:str) -> int` functions.

# Types of String

- Regular strings, which can be denoted using single quotes, double
  quotes, or triple quotes (for multi-line strings)
- *Raw* strings, which do not interpret escape characters, denoted as
  `r'[actual string]'`
- *Format* strings, which interpolate variables into optionally
  formatted fields in the string, denoted as `f'[actual string]'`
- *Byte* strings are handled differently from other strings since they
  are essentially arbitrary binary data, but share some things in common
  with character strings. You may see
  `b'[some escaped hex values here]'` and should be aware that these are
  not normal character strings. If the data represents text, however,
  you may be able it to a regular string using the `str.decode()`
  function. Conversely, you can get the raw binary of a regular string
  by using the `str.encode()` function.

# Escape Characters

  Escape character   Prints
  ------------------ ----------------------
  `\'`               Single quote
  `\"`               Double quote
  `\t`               Tab
  `\n`               Newline (line break)
  `\r`               Return
  `\\`               Backslash
  `\o<value>`        Octal value
  `\x<value>`        Hexadecimal value

# String Manipulation Methods

- Change case: `upper`, `lower`, and `title`
- Test case: `isupper`, `islower`, and `istitle`
- Test contents: `isalpha`, `isalnum`, `isdecimal`, `isspace`,
  `startswith`, and `endswith`
- Lists of strings: `join` and `split`
- Alignment: `rjust`, `ljust`, and `center`
- Remove extraneous characters: `strip`, `rstrip`, and `lstrip`
- Substrings: `find` or `index`, `replace`, and `count`
- Formatting: `format`

# Formatting Strings

Regardless of whether you are using the `format` method or format
strings (f-strings), the basic format syntax is the same.

`{}` denotes a field in which a value can be **interpolated** (i.e.
inserted). If you need a literal curly bracket, you can use double curly
brackets to escape the format syntax.

Specifying which value to interpolate into each replacement field
depends on whether you use the `format` method or f-strings. When using
the method, you should use the position of the argument you wish to
interpolate. For f-strings, you can use a variable name in scope or an
expression to be evaluated.

``` python
pi = 3.14159
e = 2.71828
'{} {}'.format(pi, e) # returns '3.14159 2.71828'
'{1} {0}'.format(pi, e) # returns '2.71828 3.14159'
f'{pi} {e}' # value is '3.14159 2.71828'
f'{2+3}' # value is '5'
```

To specify a format for the interpolated value, add a `:` to the
replacement field after the value to be interpolated, followed by a
format specification. A format specification has several options which
must be given in order if specified:

- fill and alignment: Optional fill character, followed by `<`, `>`, or
  `^` for left, right, or center justify, respectively
- sign: For numbers, `+` will always show a sign, while `-` will only
  show the sign if the value is negative. A space indicates that space
  for a sign should be left for positive numbers, but the sign displayed
  for negative numbers.
- width: Minimum number of characters that will be interpolated into the
  string, including any prefixes, separators, or other format
  characters.
- precision: Specifies how digits should be displayed. Not applicable to
  integer presentation types.
- presentation type:
  - `s` for strings (default for string values and can be omitted)
  - `b` for presenting integers in binary
  - `d` for presenting integers in decimal (default for integer values
    and can be omitted)
  - `o` for presenting integers in octal
  - `x` for presenting integers in hexadecimal
  - `n` for presenting integers with location-specific separators (i.e.
    displaying 1000 as 1,000 in North America or 1.000 in Europe)
  - `e` for presenting floats as scientific notation (displays
    precision + 1 digits, or 7 total if precision is not specified)
  - `f` for presenting floats a floating points (precision only applies
    to the digits after the point)
  - `g` for presenting floats in \`\`general\'\' format (rounds the
    value to precision significant digits; this is the default for
    floats and can be omitted)
  - `%` for presenting floats as percentages, complete with percent sign

See https://docs.python.org/3/library/string.html#format-string-syntax for a full treatment of what you can do with
format specifications