# Question 6: Count uppercase and lowercase letters in a string.
s = input()
upper = sum(c.isupper() for c in s)
lower = sum(c.islower() for c in s)
print("UPPER CASE", upper)
print("LOWER CASE", lower)
