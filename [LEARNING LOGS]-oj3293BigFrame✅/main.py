"""bigframe"""
def main():
    """main"""
    texts = []

    for _ in range(5):
        texts.append(input().rstrip())

    max_lenght = 0
    for text in texts:
        if len(text) > max_lenght:
            max_lenght = len(text)

    border_len = max_lenght + 4
    print("*" * border_len)
    for text in texts:
        space_need = max_lenght - len(text)
        pad = text + " " * space_need
        print("* " + pad + " *")
    print("*" * border_len)
main()
