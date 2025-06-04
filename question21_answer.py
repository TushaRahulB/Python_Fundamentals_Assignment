# Question 18d: Print 'tree' shape pattern using stars.
n = int(input())
for i in range(n):
    if i == 0:
        print('  ***  ')
    elif i == 3:
        print(' * *** ')
    elif i < 3:
        print(' *     ')
    elif i == 6:
        print('  * * *')
    else:
        print(' *     *')
