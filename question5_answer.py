# Question 5: Count the number of letters and digits in a string.
s = input()
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print("LETTERS", letters)
print("DIGITS", digits)
