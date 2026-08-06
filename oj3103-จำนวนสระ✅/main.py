"""จำนวนาระ"""
def main():
    """main"""
    ranges = int(input())
    count_vowels = 0
    for _ in range(ranges):
        alphabet = str(input())
        if alphabet in ["A","E","I","O","U"]:
            count_vowels += 1
    print(count_vowels)
main()
