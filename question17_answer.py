# Question 17: Validate email ID (lowercase only, one '@' allowed).
email = input()
if email.count('@') == 1 and all(c.islower() or c.isdigit() or c in ['@', '.', '_'] for c in email):
    print("Valid")
else:
    print("Invalid")
