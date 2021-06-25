"""
Restrictions on nested collections
-------------------------------------
1. Every element inside set should be hashable = [{}]
   hence we cannot take list as elements inside set = {[]} not allowed
2. Every key inside dict should be hashable.
   hence for key we cannot take list as object
Note: Indexing is not applicable inside set
"""
# merging multiple collections into one
# if u have two sets , u cant use + operator.
# if u have two dict, u cant use + operator.
# if u have 2 tuples or 2 lists then only we can use + to merge

# we can use + for two lists
l1 = [1,2,3]
l2=[1,2,3]
l3 = l1+l2
print(l3)    #l3 = [1,2,3,1,2,3]

# we can also use * to merge
l1 = [1,2,3]
l2=[1,2,3]
l3 = [*l1,*l2]
print(l3)    #l3 = [1,2,3,1,2,3]

# we can apply * to tuples also
l1 = (1,2,3)
l2=(1,2,3)
l3 = (*l1,*l2)
print(l3)

# we can also use * to merge set
l1 = {1, 2, 3}
l2= {1, 2, 3}
l3 = {*l1, *l2}
print(l3) # {1, 2, 3}

s1 = {1, 2, 3}
s2= {4, 5, 6}
s3 = {*s1, *s2}
print(s3)  # {1, 2, 3, 4, 5, 6}

# we can also use heterogeneous data to merge
s1 = {1, 2, 3}
s2= {'A', 'B', 'C'}
s3 = {*s1, *s2}
print(s3)   # {1, 2, 3, 'C', 'B', 'A'}

# we can change any data type after merge, here we are merging two sets and converting result into list
s1 = {1, 2, 3}
s2= {'A', 'B', 'C'}
s3 = [*s1, *s2]
print(s3)   # [1, 2, 3, 'C', 'B', 'A']

# merge of diff collections
s1 = {1, 2, 3}              # set
s2= ['A', 'B', 'C']         # list
s3 = ('X', 'Y', 'Z')        # tuple
s = [*s1, *s2, *s3]         # o/p=list
print(s)                    # [1, 2, 3, 'A', 'B', 'C', 'X', 'Y', 'Z']


# + operator cannot be used with dict type
s1 = {1:'I', 2:'J', 3:'k'}              # dict
s2= {4:'A', 5:'B'}                      # dict
s3 = {6:'X', 7:'Y', 8:'Z'}              # dict
s = {s1+s2+s3}                          #s = {*s1, *s2, *s3}
print(s)                                # error


# * operator can be used with dict type to merge only keys or only values
s1 = {1:'I', 2:'J', 3:'k'}              # dict
s2= {4:'A', 5:'B'}                      # dict
s3 = {6:'X', 7:'Y', 8:'Z'}              # dict
s = {*s1, *s2, *s3}
print(s)                                # if we use single * then only keys will be merged o/p = {1, 2, 3, 4, 5, 6, 7, 8}

# .values() can be used to only merge values
# s1 = {1:'I', 2:'J', 3:'k'}              # dict
# s2= {4:'A', 5:'B'}                      # dict
# s3 = {6:'X', 7:'Y', 8:'Z'}              # dict
# s = {*s1.values(), *s2.values(), *s3.values()}
# print(s)                                # only values will be merged, o/p = {'A', 'X', 'B', 'Y', 'k', 'I', 'J', 'Z'}


# ** operator should be used with dict type
s1 = {1:'I', 2:'J', 3:'k'}              # dict
s2= {4:'A', 5:'B'}                      # dict
s3 = {6:'X', 7:'Y', 8:'Z'}              # dict
s = {**s1, **s2, **s3}
print(s)                                # o/p = {1: 'I', 2: 'J', 3: 'k', 4: 'A', 5: 'B', 6: 'X', 7: 'Y', 8: 'Z'}

"""
Nested collections : collection inside collection
inside list we can take tuple
inside tuple we can take list
inside dict we can take another dict
"""

l1 = [(10,20,30), (40,50,60)]   # nested collection : list of tuples
# how to get 20 from above list?
print (l1[0])                   # o/p = (10,20,30)
print (l1[0][1])                # o/p = 20

print(l1[1][2])                 # to print 60

###### collection : tuples inside dict
d = {
    'cars' : ('Honda', 'Tata', 'Audi', 'BMW'),
    'mobiles' : ('Nokia', 'Oppo', 'MI', 'Realme')
}

# how to display 2nd car?
print(d['cars'])            # ('Honda', 'Tata', 'Audi', 'BMW')
print(d['cars'][1])         # Tata
print(d.get('cars')[1])     # Tata

# to display all mobile names
for mobile in d['mobiles']:
    print(mobile)

