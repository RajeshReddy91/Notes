# Break - used to come out of the loop when condition is satisfied
# Continue - if condition satisfies then skip current iteration (staements after cont in tht iteration will be skipped)
# and go for next iteration

for i in range(10):
    if i==7:
        print('enough loops...plz break')
        break
    print(i)

# skip if we get even number and cont
for i in range(10):
    if i%2==0:
        continue
    print(i)

lst = [1,2,3,10,4,12,8,11]
for x in lst:
    if x>9:
        continue
    print (x)

#division by zero error
lst = [10,0,2,0,13,15]
for n in lst:
    print('100/{} is : {}'.format(n,100/n))

# handling division by zero error
lst = [10,0,2,0,13,15]
for n in lst:
    if n==0:
        print('divide by zero error')
        continue
    print('100/{} is : {}'.format(n,100/n))

# loops with else (for-else, while-else)- else part will be executed only when break statement inside loop is not executed
# else is only associated with break stmt, not with continue
# else part will not run in this case
lst = [10,50,2,700,13,15]
for item in lst:
    if item > 500:
        print('cant process this item:',item)
        break
    print (item)
else:
    print('all your items processed succesfuly')

# else part will run in this case
lst = [10,50,2,70,13,15]
for item in lst:
    if item > 500:
        print('cant process this item:',item)
        break
    print (item)
else:
    print('all your items processed succesfuly')

# else part will run in this case because we have used continue here.
# but it doent make sense when we use else with continue
lst = [10,50,2,700,13,15]
for item in lst:
    if item > 500:
        print('cant process this item:',item)
        continue
    print (item)
else:
    print('all your items processed succesfuly')

