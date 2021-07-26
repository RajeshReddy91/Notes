# Anonymous functions - Nameless function

# lambda args:expression
# to find square
s = lambda n:n*n
print('square of 4 is:', s(4))
print('square of 4 is:', s(5))

# to find sum
sum = lambda a,b:a+b
print('square of 4 is:', sum(4,6))
print('square of 4 is:', sum(5,15))

# max of 2 numbers
mx = lambda a,b:a if a>b else b
print(mx(10,20))
print(mx(100,20))

# max of 3 numbers
mx = lambda a,b,c:a if a>b and a>c else b if b>c else c
print(mx(10,20,30))
print(mx(100,20,300))

# Lambda functions are best choice when we are passing a function as arg to another function
# Lambda func are useful only at that instant. If you want to use function multiple times then
# better use normal named functions
"""
1.filter(): filter values in the given sequence based on condition
filter(function, sequence)
Here function will check for condition, if function returns true then that value in the seq is considered.
If function returns false then that value will be filtered out.
o/p of function being used inside filter() should always return boolean.
here number of o/p will be less than number of i/ps since few get filtered out

2.map(): 
Here number of o/p will be equal to number of i/ps
In filter() return type should be always boolean, but in map() it can be anything.

"""
# finding even numbers using filter()
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

l = [0,10,15,20,25,30]
op=list(filter(is_even,l))
print(op)   # [0, 10, 20, 30]

# using lambda function
l=[0,5,10,15,20,25,30]
op=list(filter(lambda n:n%2==0,l))
print(op)

l=[0,5,10,15,20,25,30]
even=list(filter(lambda n:n%2==0,l))
odd=list(filter(lambda n:n%2!=0,l))
print(even)
print(odd)

# output - strings with length greater than 3 in tuple type
t=('a','aa','aaa','aaaa','aaaaa','aaaaaa')
op = tuple(filter(lambda s:len(s)>3,t))
print(op)

# map() function
def sqr(n):
    return n*n

l=[1,2,3,4,5]
op=list(map(sqr,l))
print(op)           # [1, 4, 9, 16, 25]

# using map() in lambda
l=[1,2,3,4,5]
op=list(map(lambda n:n*n,l))
print(op)           # [1, 4, 9, 16, 25]



