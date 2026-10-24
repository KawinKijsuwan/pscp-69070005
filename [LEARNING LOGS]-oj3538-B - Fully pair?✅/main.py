"""B - Fully pair"""
def main():
    """main"""
    text = input().strip()
    count = {}

    for ch in text:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    result = ""
    for ch in count:
        if count[ch] % 2:
            result = result + ch

    if not result:
        print("fully paired")
    else:
        print(result)

main()
