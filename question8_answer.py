# Question 8: Validate passwords with given constraints and print valid ones.
import re
passwords = input().split(',')
valid = []
for pwd in passwords:
    if (6 <= len(pwd) <= 12 and
        re.search(r'[a-z]', pwd) and
        re.search(r'[A-Z]', pwd) and
        re.search(r'[0-9]', pwd) and
        re.search(r'[$#@]', pwd)):
        valid.append(pwd)
print(','.join(valid))
