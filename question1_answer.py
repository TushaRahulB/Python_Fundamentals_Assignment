# Question 1: Generate a 2D array where the element at (i,j) is i*j given x rows and y columns.
x, y = map(int, input().split(','))
print([[i * j for j in range(y)] for i in range(x)])
