"""HorizontalHistogram"""
text = input()
ORDER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for ch in ORDER:
    amount = text.count(ch)

    if amount > 0:
        graph = ""

        for i in range(1,amount + 1):
            graph += "-"
            if not i % 5 and i != amount:
                graph += "|"

        print(f"{ch} : {graph}")
