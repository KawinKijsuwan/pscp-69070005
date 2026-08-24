"""a e i o u"""
def main():
    """sarakub ิ ิ"""
    text = str(input())
    vowels = ["a","e","i","o","u"]
    count = [0,0,0,0,0]

    for _ in text.lower():
        if _ in "a":
            count[0] += 1
        elif _ in "e":
            count[1] += 1
        elif _ in "i":
            count[2] += 1
        elif _ in "o":
            count[3] += 1
        elif _ in "u":
            count[4] += 1

    for i in range(5):
        if count[i] > 0:
            print(f"{vowels[i]} : {count[i]}")
main()
