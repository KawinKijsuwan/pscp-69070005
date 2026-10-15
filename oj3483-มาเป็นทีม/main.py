"""มาเป็นทีม"""
n, m = map(int, input().split())

if n < 1 or n > 10 or m < 1 or m > 20:
    print("Data Incorrect")
else:
    scores = []
    is_incorrect = False

    for _ in range(n):
        team_score = list(map(int, input().split()))

        if len(team_score) != m:
            is_incorrect = True
            break

        for score in team_score:
            if score < 0 or score > 100:
                is_incorrect = True

        scores.append(team_score)

    if is_incorrect:
        print("Data Incorrect")
    else:
        total_score = 0

        for i in range(n):
            team_total = sum(scores[i])
            average = team_total / m
            maximum = max(scores[i])

            print(f"Team {i + 1}: Average = {average:.2f}, Max = {maximum}")

            total_score += team_total

        print("Total Score of All Teams =", total_score)
