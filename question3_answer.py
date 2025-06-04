# Question 3: Accept a sequence of whitespace-separated words and print after removing duplicates and sorting.
words = input().split()
print(' '.join(sorted(set(words))))
