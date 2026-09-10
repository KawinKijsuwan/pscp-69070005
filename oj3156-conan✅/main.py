"""conan"""
def main():
    """main"""
    text = input()
    k = int(input())
    result = ""

    for ch in text:
        shifted = (ord(ch) - ord('a') + k) % 26
        result += chr(shifted + ord('a'))
    print(result)
main()
