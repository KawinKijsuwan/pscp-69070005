"""examscore"""
def main():
    """examscore"""
    rabbits = int(input())
    top_score = 0
    num_topscore = 0
    for i in range(rabbits):
        score = int(input())
        if score > top_score:
            top_score = score
            num_topscore = 1
        elif score == top_score:
            num_topscore = num_topscore + 1
    print(top_score)
    print(num_topscore)
main()
