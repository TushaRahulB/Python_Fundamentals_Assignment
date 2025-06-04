# Question 13: Count unique pairs of ones in a binary string.
s = input()
count = 0
ones = [i for i, c in enumerate(s) if c == '1']
for i in range(len(ones)):
    for j in range(i + 1, len(ones)):
        count += 1
print(count)
