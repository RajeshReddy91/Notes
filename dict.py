"""
sorted() method sorts the given sequence either in ascending order or in descending order and always return
the a sorted list. This method does not effect the original sequence.

sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the
original sequence. Moreover, sort() is a method of list class and can only be used with lists.
"""

# Dup keys are not allowed, but dup values are allowed
# If we try to add key-value where this key is already present, then old value will be replaced with new value.
# order is not applicable and all elements will be inserted based on hash of keys.
# hence indexing and slicing are not applicable
# keys and values can be heterogeneous objects. ie. dict = {100:'rjesh', reddy:'lname'}
# dict is mutable

"""
1.dict()
2.len()
3.clear()
4.get()
5.pop()
6.popitem()
7.keys()
8.values()
9.items()
10.setdefault()
11.update()
12.copy()
"""
#***** Dict comprehension *************

# we can create dict in following ways
#1
d={}
print(type(d))
print(d)
#2
e = dict()
print(type(e))
print(e)

# adding key-value pairs
d={}
d['fname'] = 'rajesh'
d['lname'] = 'reddy'
d['addr'] = 'karnataka'
d['fname'] = 'raj'       # if we enter dup key then value will be updated with new value
print(d)

d = {'fanme' : 'rajesh',
     'lanme' : 'reddy',
        '578975989' : 'phone_num'}
print (d)

# How to access data from dict? by using 'key'
d = {'fname' : 'rajesh',
     'lname' : 'reddy',
        '578975989' : 'phone_num'}

print(d['fname'])


# How to access data from dict? by using 'key'
d = {'fname' : 'rajesh',
     'lname' : 'reddy',
        578975989 : 'phone_num'}
# print (d['fname'])
key = eval(input('enter any key : '))     # if we use int for type conversion or just input then we will get error
if key in d:
    print (d[key])
else:
    print ('specified key is not present in dict')

# How to add key-values to empty dict?

mlist = {}
while True:
    name = input('enter name os stdnt :')
    marks = int(input('enter stdnt marks : '))
    mlist[name] = marks
    print('marks entered succesfuly')
    option = input('do u want add another entery?[Yes|No]')
    if option.lower()=='no':
        break
print('these are the marks entered')
print(mlist)

# OR - when u enter valid option yes|no

mlist = {}
while True:
    name = input('enter name os stdnt :')
    marks = int(input('enter stdnt marks : '))
    mlist[name] = marks
    print('marks entered succesfuly')
    option = input('do u want add another entery?[Yes|No]')
    while True:
        if option.lower()=='no':
            option='no'
            break
        elif option.lower()=='yes':
            option='yes'
            break
        else:
            option=input('plz enter valid i/p [yes|no]:')
    if option=='no':
        break
print('these are the marks entered')
print(mlist)


# simlified

mlist = {}
while True:
    name = input('enter name os stdnt :')
    marks = int(input('enter stdnt marks : '))
    mlist[name] = marks
    print('marks entered succesfuly')
    option = input('do u want add another entery?[Yes|No]')
    while True:
        if option.lower() in ('yes','no'):
            break
        else:
            option=input('plz enter valid i/p [yes|no]:')
    if option=='no':
        break
print('these are the marks entered')
print(mlist)

# more simplified
mlist = {}
while True:
    name = input('enter name os stdnt :')
    marks = int(input('enter stdnt marks : '))
    mlist[name] = marks
    print('marks entered succesfuly')
    option = input('do u want add another entery?[Yes|No]')
    while option.lower() not in ('yes','no'):
          option=input('plz enter valid i/p [yes|no]:')
    if option=='no':
        break
print('these are the marks entered')
for x in mlist:
    print('{}\t\t{}'.format(x,mlist[x]))

# insert and update in dict
d = {100 : 'raj', 200 : 'reddy', 300 : 'navalli'}
print(d)

d[400]='xyz'
print(d)

d[100] = 'rajesh'
print(d)

# to delete
del d[100]    # we can also use d.pop[key] - after executing it will display deleted key

# delete arbitrary item and display
d.popitem()

# to get ascii value of alphabets and delete
# del and pop u can use only when u know key, popitem() can be used without knowing key
i=0
d={}
while i<26:
    d[chr(65+i)] = 65+i
    i+=1
print (d)

while len(d) != 0:
    print('processing item:',d.popitem())
print('now d is empty',d)

# to delete whole dict
d.clear()  #o/p {}

# if we use "del d" then whole dict will be deleted.
del d

############ important methods and functions related to dict
d=dict()
print(d)  # will print empty dict

e=dict({100:'a', 200:'b', 300:'c'})
print(e)

# using list of tuples
f=dict([(1,'a'),(2,'b'),(3,'c')])
print(f)

# using tuples of tuples
g=dict([(1,'a'),(2,'b'),(3,'c')])
print(g)

# using list of list
h=dict([[1,'a'],[2,'b'],[3,'c']])
print(h)

# len(d) - returns number of items (key-value pairs) in the dict
# to get values associated with keys
# d[key] - will throw error if key is not present
# or d.get(key) - will return "None" if key is not present

# if key is not avaiable then print return NA
d = {1:'a', 2:'b', 3:'c', 4:'c'}
print(d.get(1, 'NA'))
print(d.get(5, 'NA'))     # if key 1 is not avaiable then it will return NA


# interview question - get only keys and sort it

# k = d.keys()  # k will hold all the keys which are in dict d, k will be of type dict_keys
# will get A-Z with their ascii values
i=0
d={}
while i<26:
    d[chr(65+i)] = 65+i
    i+=1

for k in d.keys():     # interview answer
    print(sorted(k))

"""
The primary difference between the list sort() function and the sorted() function is that the sort() function
 will modify the list it is called on. The sorted() function will create a new list containing a sorted version 
 of the list it is given. The sorted() function will not modify the list passed as a parameter. If you want to 
 sort a list but still have the original unsorted version, then you would use the sorted() function. 
 If maintaining the original order of the list is unimportant, then you can call the sort() function on the list.

A second important difference is that the sorted() function will return a list so you must assign the returned
data to a new variable. The sort() function modifies the list in-place and has no return value.
"""
d.keys()
d.values()  # will give u all values in the dict and d will be of type dict_values
d.items()   # will return key-value pairs, return type will be dict_items in the form of list of tuples

# to access both keys and values
d = {1:'a', 2:'b', 3:'c', 4:'c'}

for k, v in d.items():
    print('{}:{}'.format(k,v))

# if the specified key is available, then it will display corresponding value,
# if the specified key is not available, then provided key-value pair will be added as a new item to the dict
d = {1:'a', 2:'b', 3:'c', 4:'c'}
print(d.setdefault(1,'d')) #if  key=1 is there then it will display its value,
print(d)
print(d.setdefault(5,'d')) # if its not there then key=5 with value=d will be added
print(d)

# add all the items present in d2 into d1
d1 = {1:'a', 2:'b', 3:'c', 4:'c'}
d2 = {5:'d', 6:'e', 7:'f', 8:'g'}

print(d1)
d1.update(d2)
print(d1)

# if key present in d2 is already there in d1 then value of that key in d1 will be updated with key=value present in d2
# update will try to replicate whatever is present in d2 into d1
d1 = {1:'a', 2:'b', 3:'c', 4:'c'}
d2 = {4:'d', 6:'e', 7:'f', 8:'g'}

print(d1)
d1.update(d2)
print(d1)

# d2 = d1 ==> duplicate reference variable and aliasing
# d2 = d1.copy() ==> duplicate object and cloning

d1 = {1:'a', 2:'b', 3:'c', 4:'c'}

d2=d1.copy()
print(d1)  # both d1 and d2 will have same values but memory allocation will be different
print(d2)
print(id(d1))
print(id(d2))
print(d1 is d2)

d2=d1
print(d1 is d2)  # True
print(id(d1))    # both d1 and d2 will have same memory allocation
print(id(d2))
d1[1]='d'    # updating key value in d1
print(d1)
print(d2)    # same will be reflected in d2

#wap to find number of occurrence of vowels in a given word

#************* Dict comprehension *************
# {1:1, 2:4, 3:9, 4:16. 5:25}
# d = { key:value for x in range(1, 6) | if condition}

d = { x:x*x for x in range(1,6) }
print(d)

alpha = { x:chr(64+x) for x in range(1,26) }  # print alphabets
print(alpha)

#######################################
# wap to enter stdnt name and marks, and display marks by taking stdnts name as input

n = int(input('plz enter number of students:'))
d={}
for i in range(n):
    name = input('enter stdnt name:')
    marks = int(input('enter marks: '))
    d[name] = marks
print('all stdnts data entered')
while True:
    name = input('enter stdnt name to get marks : ')
    if name in d:
        print('marks obtained by {} is : {}'.format(name, d[name]))
    else:
        print('invalid name, plz enter correct name')

    option = input('Do you want to get marks of another student?[yes|no]')
    while option.lower() not in ['yes','no']:
        option = input('plz enter valid option[yes,no]: ')
    if option.lower() == 'no':
        break
print('thanks for using our application')



