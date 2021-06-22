#i/o statements
"""
to read dynamic input from keyboard
1. raw_input() = this function will always return o/p as string type
type casting is required

2. input() = whatever i/p type is o/p will be of same type
type casting is not required

above 2 are aplicable for only python-2.
In python-3 we have only one function to read i/p from keyboard, ie. input().
But this function will only return str type so type casting is required.
"""

x = input('enter some value:')
print(type(x))  # always return str type
i=int(x)        # will return int type
print(type(i))

# wap to read 2 numbers and print its sum
a = int(input('Enter value of a :'))
b = int(input('Enter value of b :'))
print('Entered values are',a, b)
print('sum = ', a+b)

# in a single line
print('sum = ', int(input('Enter value of a :'))+int(input('Enter value of b :')))

"""
bool(str)
if str is non-empty string then it returns True
if str is empty string then it returns False
"""
enum = int(input('enter emp number:'))
ename = input('enter emp name:')
esal = float(input('enter emp sal:'))
eaddr = input('enter emp addrs:')
married = bool(input('emp married?[True|False]:'))
# though u put married = False it will show you True, coz bool('non-empty string') is always true

print('Please confirm your information:')
print('emp number:', enum)
print('emp name:', ename)
print('emp sal:', esal)
print('emp addrs:', eaddr)
print('Married:', married)

"""
eval('str') function return type will be always same as the type of value inside str(it always takes string as argument)
ex - 
eval('10') -- int    # return type
eval('10.5') -- float  # '10.5' is a string but still return type will be float
eval('True') -- boolean
eval('False') -- boolean   
"""
enum = eval(input('enter emp number:'))
ename = input('enter emp name:')
esal = eval(input('enter emp sal:'))
eaddr = input('enter emp addrs:')
married = eval(input('emp married?[True|False]:'))  # eval will solve above issue

# eval performance is slower than type casting

print('Please confirm your information:')
print('emp number:', enum)
print('emp name:', ename)
print('emp sal:', esal)
print('emp addrs:', eaddr)
print('Married:', married)

x = '10 20 30'
l = x.split()  # split is always applied on str object and return type is list
print (l)

# List comprehension
a, b, c = [int(x) for x in input('enter three numbers: ').split()]
print(a, b, c)
print(type(a), type(b), type(c))
print(a*b*c)


# command line arguments

from sys import argv

print('number of CL args are :', len(argv))
print('list of CL args are', argv)
print('first arg is', argv[0])
print('second arg is', argv[1])
for x in argv:
    print (x)


# to get the sum of 3 numbers using CL args
# we can use as many args we want, this method is useful when we dont know how many args customer will use 
from sys import argv
print (argv)
args = argv[1:]
sum=0
for x in args:
    n=int(x)
    sum=sum+n

print('sum=',sum)

