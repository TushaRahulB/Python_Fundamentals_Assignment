# Question 9: Sort tuples by name, age, and score.
entries = []
while True:
    try:
        line = input()
        if not line:
            break
        entries.append(tuple(line.split(',')))
    except:
        break
entries.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(entries)
