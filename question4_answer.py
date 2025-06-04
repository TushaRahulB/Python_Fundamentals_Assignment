# Question 4: Find all numbers between 1000 and 3000 where every digit is even.
print(','.join([str(i) for i in range(1000, 3001) if all(int(d) % 2 == 0 for d in str(i))]))
