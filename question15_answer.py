# Question 15: Find number of combinations C(n-m+1, m).
from math import comb
n = int(input("n="))
m = int(input("m="))
print(comb(n - m + 1, m))
