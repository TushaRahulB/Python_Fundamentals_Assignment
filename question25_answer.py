# Question 21: Check if a number is an Armstrong number.
num = int(input())
power = len(str(num))
if sum(int(d)**power for d in str(num)) == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
