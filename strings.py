s = ''''khvkjhvkjndskn'''
print (s)

'''2 ways to access characters from a word
1. using incex
2. using slice operator'''

s1 = 'rajesh'
print(s1[5] , s1[-1])

# print index and character
ch = input('enter any character: ')
n=0
for i in ch:
    print('charcter at {} is {}'.format(n, i))
    n=n+1

# character at both +ve and -ve index
ch = input('enter any character: ')
n=0
for i in ch:
    print('charcter at positive index {} and at negative index {} is {}'.format(n,n-len(ch), i))
    n=n+1


# By using slice , s[begin:end:step]
s = 'Hi how are you'
print(s[1:5])

# By using slice , s[begin:end:step]
s = 'Hi how are you'
print(s[:5])    # from begining to 5th place


# By using slice , s[begin:end:step]
s = 'Hi how are you'
print(s[5:])    # from 5th place to end


# By using slice ,pallendrome
s = 'GADAG'
print(s[-1::-1]) #s[::-1]


# Slice will not give "out of range error" if u give end index more than length of string
s = 'GADAG'
print(s[:10000])

# while using backward slicing, default step value will not be there.... we have to specify it
# in forward slicing default step value will be 1
s = 'rajesh'
print(s[-1::])

# forward and backward string
s = input('enter any string : ')
i=0
n=len(s)
while i<n:
    print(s[i])
    i+=1
print()
i=-1
while i>=-n:
    print(s[i])
    i-=1

# OR
s = input('enter any string : ')
for x in s[::]:
    print(x)

for x in s[::-1]:
    print(x)