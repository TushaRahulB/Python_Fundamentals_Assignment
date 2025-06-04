# Question 11: Perform simple run-length encoding on a string.
s = input().lower()
result = ''
i = 0
while i < len(s):
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
        i += 1
    result += s[i] + str(count)
    i += 1
print(result)
