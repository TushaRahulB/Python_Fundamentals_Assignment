# Question 18a: Print triangle pattern with consecutive numbers.
n = int(input())
num = 1
for i in range(1, n + 1):
    print(' * '.join(str(num + j) for j in range(i)))
    num += i
