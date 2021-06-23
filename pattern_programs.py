### display 5 * in a row
n = int(input('enter any number:'))
for i in range(n):
    print('*', end=' ')
print()
print('* ' * n)

### display * in square pattern
n = int(input('entern n value:'))
i = 0
while i<n :
    print('* ' * 5)
    i=i+1

# OR
n = int(input('entern n value:'))
for i in range(n):
    print('* ' * n)

# OR
n = int(input('entern n value:'))
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()   # print('\n') will give two blank lines


### nxn square
n = int(input('entern n value:'))
for i in range(n):
    sym = str(n)+' '
    print(sym * n)


# 1 1 1
# 2 2 2
# 3 3 3
n = int(input('entern n value:'))
for i in range(n):
    sym = str(i+1)+' '
    print(sym * n)

# A A A
# B B B
# C C C

n = int(input('entern n value:'))
for i in range(n):
    print((chr(65+i)+' ')*n)

# 1 2 3
# 1 2 3
# 1 2 3
n = int(input('entern n value:'))
for i in range(n):
    j=0
    while (j<n):
        print(j+1, end=' ')
        j=j+1
    print()
print()
print('using for loop')

for i in range(n):
    for j in range(n):
        print(j+1, end=' ')
    print()


# 3 2 1
# 3 2 1
# 3 2 1
n = int(input('enter n value: '))

for i in range(n):
    for j in range(n,0,-1):
        print(j, end=' ')
    print()
print()
# OR
for i in range(n):
    for j in range(n):
        print(n-j, end=' ')
    print()

# *
# * *
# * * *
n = int(input('n value: '))
for i in range(n):
    print('* ' * (i + 1))

#OR
n = int(input('n value: '))
for i in range(n):
    for j in range(i+1):
        print('* ', end=' ')
    print()

# 3
# 3 2
# 3 2 1
n = int(input('n value: '))
for i in range(n):
    for j in range(i+1):
        print(n-j, end=' ')
    print()

# pyramid
#   *
#  * *
# * * *
#* * * *
n = int(input('n value:'))
for i in range(n):
    print(' '*(n-i-1),end='')
    print('* '*(i+1))








