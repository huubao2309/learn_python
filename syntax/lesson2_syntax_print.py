# Lesson 2: https://www.youtube.com/watch?v=XMeYyJfbgpY&list=PLux-_phi0Rz0Ngc01o_GYe0JUGjL1yIAm&index=2
# Syntax: print(object, sep = seperator, end = end)
# In there:
# + Object: Object in Python (string, int, double,....)
# + Seperator: Character (/, !, ...) (default seperator = " ")
# + End: End Character, if param is null, "\n" will be set default

## Example 1:
print('abc')
# -> abc

## Example 2: no "seperator" and new line
a = 100
b = 200
c = 300
print(a, b, c)
print('Test Example 2')
# -> 100 200 300
# -> Test Example 2

## Example 3: use "seperator"
a = 100
b = 200
c = 300
print(a, b, c, sep = "--")
print('Test Example 3')
# -> 100--200--300
# -> Test Example 3

## Example 4: use "end"
a = 100
b = 200
c = 300
print(a, b, c, sep = "--", end = "!!!")
print('Test Example 4')
# -> 100--200--300!!!Test Example 4

## Example 5: use "end" and "\n"
a = 100
b = 200
c = 300
print(a, b, c, sep = "--", end = "!!!\n")
print('Test Example 4')
# -> 100--200--300!!!
# -> Test Example 4

