# Question 20: Compare patient health metrics with ideal values and show differences.
ideal = {"Sugar level":15, "Blood pressure":32, "Heartbeat rate":71, "weight":65, "fat percentage":10}
patient = {}
for k in ideal:
    val = int(input(k + ": "))
    patient[k] = val
diff = {k: patient[k] - ideal[k] for k in ideal}
print(diff)
for k, v in diff.items():
    print(f"{k} {v}")
    if v < 0:
        print(f"{k} is {abs(v)} less than the ideal value")
    elif v > 0:
        print(f"{k} is {abs(v)} more than the ideal value")
