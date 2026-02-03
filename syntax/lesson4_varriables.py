# Lesson 4: https://www.youtube.com/watch?v=XeURcCz160o&list=PLux-_phi0Rz0Ngc01o_GYe0JUGjL1yIAm&index=4
# Varriable in Python

a = 100
print('Type:', type(a))

d = 3.25
print('Type:', type(d))

str = "This is table"
print('Type:', type(str))

## --> Type: <class 'int'>
## --> Type: <class 'float'>
## --> Type: <class 'str'>

### Note: In Python, you don't need to define type of varriable 
### Eg: C/C++; int a = 100;


### Note: Name of varriable
### 1. No space in name. E.g: dien tich = 1.25
### 2. No start by number. E.g: 1name = "Table"
### 3. No special character. E.g: name# = "Apple"
### 4. Uppercase and lowercase in Python is difference. E.g: name and Name
a = 50
A = 100
print('a, A = ', a, A)
## --> a, A =  50 100

dientich = 10
dienTich = 20
print('dientich, dienTich = ', dientich, dienTich)
## --> dientich, dienTich =  10 20

## Example 1: Round double/float
a = 28.041234
print('Round1:', '%.2f' % a)
## --> Round1: 28.04
print('Round2:', round(a, 2))
## --> Round2: 28.04
print('Round3:', '{:.2f}'.format(a))
## --> Round3: 28.04

## Example 2: bool: True/False
a = True
b = False
print('Type a:', type(a))
print('Type b:', type(b))
## --> Type a: <class 'bool'>
## --> Type b: <class 'bool'>

### Example 3: String with """ """
str = """
- Nguyen
- Van
- A
"""
print('Str:', str)
## --> Str: 
## --> Nguyen
## --> Van
## --> A

### Example 4: 
str = '8123'
a = int(str)
print('Result str:', str, ', Result a:', a, ', With type:', type(a))
## --> Result str: 8123 , Result a: 8123 , With type: <class 'int'>