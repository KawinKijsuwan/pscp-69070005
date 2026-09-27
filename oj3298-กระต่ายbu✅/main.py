"""BUU shout checker - basic version"""
def main():
    """main"""
    s = input()
    s_upper = s.upper()
    n = len(s)

    if "BUU" in s_upper:
        max_u = 0
        for i in range(n):
            if s_upper[i] == "B":
                count = 0
                j = i + 1
                while j < n:
                    if s_upper[j] == "U":
                        count = count + 1
                        j = j + 1
                    else:
                        break
                if count > max_u:
                    max_u = count
        print("Yes", max_u)

    elif "B" in s_upper:
        first_b = 0
        for i in range(n):
            if s_upper[i] == "B":
                first_b = i
                break

        result = ""
        for i in range(n):
            if i <= first_b:
                result = result + s[i]
            else:
                result = result + "U"
        print(result)

    else:
        buu = "BUU"
        result = ""
        for i in range(n):
            result = result + buu[i % 3]
        print(result)

main()
