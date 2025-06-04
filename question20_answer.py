# Question 18c: Print symmetrical triangle pattern using numbers.
n = int(input())
num = 1
lines = []
for i in range(1, n + 1):
    line = ' * '.join(str(num + j) for j in range(i))
    lines.append(line)
    num += i
for line in lines:
    print(line)
for line in reversed(lines[:-1]):
    print(line)
