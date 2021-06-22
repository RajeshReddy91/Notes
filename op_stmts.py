# output statements
print('1\n2')
print('hi',end='*')
print('hello','hi',sep='!', end='')
print('how','r','u',sep='*',end='\n')

# print with formatted string

"""
these are called formatters
%i - int
%d - int
%f - float
%s - string
"""

a=10
b=20
c=30

print('a value is %i' %a)
print('b value is %d' %b)

name = 'rajesh'
l = [1,2,3,4,5]
print('hi %s, the list of items are %s' %(name, l))   #first %s = name, second %s = list


# print with {} - replacement operator
fname='rajesh'
lname='reddy'
sal=10000
print('hi {x}, your lname is {y} and sal is {z}'.format(x=fname, y=lname, z=sal))  # here order of args is not important
print('hi {0}, your lname is {1} and sal is {2}'.format(fname, lname, sal)) # here order of args is important
print('hi {0}, your lname is {0} and sal is {0}'.format(fname, lname, sal))
print('hi {}, your lname is {} and sal is {}'.format(fname, lname, sal))

