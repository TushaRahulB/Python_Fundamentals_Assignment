# Question 7: Compute net amount from a series of bank deposits and withdrawals.
total = 0
while True:
    try:
        line = input()
        if not line:
            break
        op, val = line.split()
        if op == 'D':
            total += int(val)
        elif op == 'W':
            total -= int(val)
    except:
        break
print(total)
