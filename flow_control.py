"""
Three categories of flow control statements
1. Conditional statements or selection statements
if, if-else, if-elif-else, if-elif

2. Iterative statements or loops
for, while  # when statements are needed to be repeatedly executed


3. Transfer statements
break, continue
pass, del
"""
# wap to find even or odd
a = int(input('Enter any number:'))
if a%2==0:
    print('Entered number is even')
else:
    print('Entered number is odd')

x = int(input('Enter any number:'))
if x>=1 and x<=100:
    print('Number is btw 1 and 100')
else:
    print('Number is not btw 1 and 100')


a = input('Enter any word:')
i=0
for x in a:
    print('index of the character',x,'is',i)
    i+=1

# to get odd number btw 1 to 21
for x in range(1,21,2):
    print(x)

# to display numbers from 10 to 1

for x in range(10,0,-1):
    print(x)

# sum of first n numbers

n = int(input('enter any value :'))
i=0
sum=0

while(i<=n):
    sum=sum+i
    i=i+1
print('sum of {} numbers is:{}'.format(n,sum))

# while loop will not end untill u give i/p as sunny

x = ''
while(x != 'sunny'):
    x = input('enter ur fvr8 actress: ')

# using break
i=0
x = ''
while(x != 'raveena'):
    x = input('guess my fvr8 actress, you have max 3 attempts: ')
    i = i+1
    if i==3:
        print ('you have attempted max number of times')
        break

# infinte loop
i=0
while True:
    i=i+1
    print(i)

# Nested loops

for i in range(4):
    for j in range(4):
        print(i,j)
