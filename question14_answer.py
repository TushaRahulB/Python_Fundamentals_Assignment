# Question 14: Currency change calculator using greedy algorithm.
currencies = list(map(int, input("Enter valid_currency: ").split(',')))
money = int(input("Money: "))
currencies.sort(reverse=True)
for c in currencies:
    if money >= c:
        count = money // c
        print(f"{c}-{count}")
        money -= c * count
