# Question 16: Rock-paper-scissors game simulation till one player scores 5.
score_a = score_b = 0
while score_a < 5 and score_b < 5:
    a = input("Player A: ").lower()
    b = input("Player B: ").lower()
    if a == b:
        print("DRAW")
    elif (a == 'stone' and b in ['scissor', 'cut']) or          (a == 'paper' and b == 'stone') or          (a == 'scissor' and b == 'paper') or          (a == 'cut' and b == 'paper'):
        score_a += 1
        print("Player A wins")
    else:
        score_b += 1
        print("Player B wins")
