"""
def func_name(parameters):
    """u can include doc string also"""
    business logic
    return value
Dry Principle : Don't repeat yourself
Built-in functions and UDF

"""

def calc(a,b):
    print('sum:', a+b)
    print('diff',a-b)
calc(3,4)
calc(5,3)

# without parameters
def wish():
    print('hello')
wish()

# with string type as parameter
def greet(name):
    print('hello {}'.format(name))

greet('rajesh')

# dynamic input
def greet(name):
    print('hello {}'.format(name))

name = input('enter ur name: ')
greet(name)

#using return
def add(a,b):
    return a+b

result = add(10,20)
print(result)

# Every Function in python will always return some value, if not then it will return "None"
def f1():
    print('hello')
result = f1()
print(result)   # here we are not returning anything, but printing result

# taking user input
def even_odd(n):
    if n%2 == 0:
        print('given number is even')
    else:
        print('given number is odd')

even_odd(int(input('enter value of n:')))

#########
def show(seq):
    for x in seq:
        print(x)

show('durga')
show(range(1,6))

####### this will return None
def show(seq):
    for x in seq:
        return x
    result = x
    print(result)

show('durga')
show(range(1,6))

############# imp ##############
def fact(n):
    result=1
    while n>1:
        result=result*n
        n=n-1
    return result

print(fact(5))

for i in range(1,11):
    print('fact of {} is:{}'.format(i, fact(i)))

# Note:We can return multiple values in python
def calc(a,b):
    sum = a+b
    sub = a-b
    return sum,sub   # return type will be tuple (sum, sub)

t=calc(10,20)
print(type(t))   # return type will be tuple

x,y = calc(10,20)    # here tuple will be unpacked into x and y
print('sum is:', x)
print('sub is:', y)

"""
Types of arguments/parameters:
1. Positional arguments: ex- calc(a,b) - number ofargs must be matched with that described while creating functions
2. Keyword arguments - Passing arg values by parameter name, calc(a=10, b=20) or calc(b=20, a=10)
3. Default arguments - while calling function if we don't pass arg then by default it will take guest as arg. 
while declaring functions default args should be the last args, we cannot specify general args after default args.
def wish(msg='HI', name='guest'):   # valid
    print(msg,name) # wish() - o/p=HI guest

def wish(msg, name='guest') # valid
def wish(msg='HI', name)    # error

4. Variable length arguments - we can call this func using any number of args
def f(*x):
    print('hi')

f()             # valid
f(1)            # valid
f(1,2,3,4,5)    # valid

def f(n, *s):   # valid
    print(n)
    print(s)

def f(*n, s):   # valid
f(1,2,3,4, s=5) # valid

def f(n=10,*s):
    print(s)
    print(n)

f(1,2,3,4,5)
(2, 3, 4, 5)
1

f(n=20, 1,2,3,4)  
(1, 2, 3, 4)
20

Note: **x - can be used to pass any number of key-value pairs (x will become dict)
For readability we can use as **kwargs (key-word args)
kwargs should be ur last argument
"""

def display(**kwargs):
    print(type(kwargs))
    print(kwargs)

display(name='rajesh', number=2985798237, lname='reddy')

#o/p
#<class 'dict'>
#{'name': 'rajesh', 'number': 2985798237, 'lname': 'reddy'}

def display(**kwargs):
    for k,v in kwargs.items():
        print("{}={}".format(k,v))

display(name='rajesh', number=2985798237, lname='reddy')
#o/p
#name=rajesh
#number=2985798237
#lname=reddy

"""
Types of variables:
1. Global - Variables declared outside of the functions, and are available for all the functions.
2. Local - Variables declared inside the functions, and are available for only that function.
"""

# global variable
a=10
def f1():
    print(a)
def f2():
    print(a)

f1()
f2()

# local variable
def f1():
    a=10
    print(a)
def f2():
    print(a)

f1()    # o/p=10
f2()    # error - name 'a' is not defined

# both local n global
a=7             #global

def f1():
    a=10        #local
    print(a)
def f2():
    print(a)

f1()            #10
f2()            #7

# using global key word
a=7             #global
def f1():
    global a    #global a=10 - error
    a=10        #global
    print(a)
def f2():
    print(a)

f1()            #10
f2()            #10

# printing global value of variable using "globals()"
a=7             #global
def f1():
    a=10        #local
    print('Local variable value:',a)
    print('Global variable value:',globals()['a'])
f1()

###############
a=10                    # here both a and b are global variables coz they are declared outside the function
for i in range(1):
    b=20
print(a,b)  # o/p - 10 20

# Recursive function - A function that calls itself  ***** imp
def fact(n):
    print('finding factorial of :',n)
    if n==0:
        result=1
    else:
        result = n*fact(n-1)      # recalling fact funtion
    return result

print('fact(5) is:',fact(5))

"""
finding factorial of : 5
finding factorial of : 4
finding factorial of : 3
finding factorial of : 2
finding factorial of : 1
finding factorial of : 0
fact(5) is: 120
"""
###############################
def fact(n):
    print('finding factorial of :',n)
    if n==0:
        result=1
    else:
        result = n*fact(n-1)      # recalling fact funtion
    print('completion of finding factorial of {} and result is {}'.format(n, result))
    return result

print('fact of 5 is:', fact(5))
"""
finding factorial of : 5
finding factorial of : 4
finding factorial of : 3
finding factorial of : 2
finding factorial of : 1
finding factorial of : 0
completion of finding factorial of 0 and result is 1
completion of finding factorial of 1 and result is 1
completion of finding factorial of 2 and result is 2
completion of finding factorial of 3 and result is 6
completion of finding factorial of 4 and result is 24
completion of finding factorial of 5 and result is 120
fact of 5 is: 120
"""
