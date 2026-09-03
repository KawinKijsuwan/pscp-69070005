"""ระบบคิดคะแนนเกมออนไลน์"""
def main():
    """main"""
    base_score = int(input())
    bonus_score = int(input())
    days_play = int(input())
    mutiple_score = 1
    score_password = 0
    days_password = 0

    if days_play >= 3:
        mutiple_score = 1.5
    total_score = (base_score + bonus_score)*mutiple_score
    if total_score >= 1500:
        score_password = 5
    elif total_score >= 1000:
        score_password = 4
    elif total_score >= 500:
        score_password = 3
    elif total_score < 500:
        score_password = 2
    elif total_score < 200:
        score_password = 1
    if score_password == 5 and days_play >= 7:
        days_password = 99
    elif score_password == 4 and bonus_score > 300:
        days_password = 88

    print(total_score)
    print(score_password)
    print(days_password)
main()
