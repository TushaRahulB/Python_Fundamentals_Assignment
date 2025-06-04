# Question 12: Find letter pairs with digit sum between them equal to 9.
import re
s = input()
pairs = []
for i in range(len(s)):
    if s[i].isalpha():
        for j in range(i + 1, len(s)):
            if s[j].isalpha():
                digits = re.findall(r'\d+', s[i+1:j])
                if sum(map(int, digits)) == 9:
                    pairs.append((s[i], s[j]))
                break
for p in pairs:
    print(','.join(p))
