# Question 23: Check if a number is a perfect number.
n = int(input())
if sum(i for i in range(1, n) if n % i == 0) == n:
    print("Perfect number")
else:
    print("Not a perfect number")
