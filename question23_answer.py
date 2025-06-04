# Question 19: Circularly rotate a string left or right by N times.
mode = int(input())
s = input().strip().replace("'", "")
times = int(input())
for _ in range(times):
    if mode == 1:
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]
    print(s)
