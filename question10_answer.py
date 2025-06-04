# Question 10: Calculate distance from the origin based on movement commands.
import math
x = y = 0
while True:
    try:
        line = input()
        if not line:
            break
        direction, steps = line.split()
        steps = int(steps)
        if direction == 'UP':
            y += steps
        elif direction == 'DOWN':
            y -= steps
        elif direction == 'LEFT':
            x -= steps
        elif direction == 'RIGHT':
            x += steps
    except:
        break
print(round(math.sqrt(x**2 + y**2)))
