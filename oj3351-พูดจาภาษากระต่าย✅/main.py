text = input().upper()

only_it = True

for ch in text:
    if ch != "I" and ch != "T":
        only_it = False
        break

if only_it:
    print("unknown", len(text))

else:
    i = 0
    max_a = 0

    while i < len(text):
        if text[i] == "R":
            if i + 1 == len(text):
                print("no", i)
                break

            if text[i + 1] != "A":
                print("no", i + 1)
                break
            count_a = 0
            i += 1

            while i < len(text) and text[i] == "A":
                count_a += 1
                i += 1

            if count_a > max_a:
                max_a = count_a

        elif text[i] == "B":
            if i + 1 == len(text):
                print("no", i)
                break

            if text[i + 1] != "I" and text[i + 1] != "T":
                print("no", i + 1)
                break

            i += 1

            while i < len(text) and (text[i] == "I" or text[i] == "T"):
                i += 1

        elif text[i] == "I" or text[i] == "T":
            i += 1

        else:
            print("no", i)
            break

    else:
        print("yes", max_a)
