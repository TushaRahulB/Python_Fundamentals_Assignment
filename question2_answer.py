# Question 2: Accept a comma-separated sequence of words and print them in sorted order.
items = input().split(',')
items.sort()
print(','.join(items))
